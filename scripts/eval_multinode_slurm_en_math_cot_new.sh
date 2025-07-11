#!/bin/bash
#SBATCH --job-name=finemath_eval
#SBATCH --output=/mbz/users/fan.zhou/backup/slurm/job.%J.log
#SBATCH --partition=mbzuai
#SBATCH --error=/mbz/users/fan.zhou/backup/slurm/job.%J.err
#SBATCH --time=50:00:00
#SBATCH --nodes=5
#SBATCH --ntasks-per-node=8
#SBATCH --gres=gpu:8
#SBATCH --exclusive
#SBATCH --exclude=g42-odin-h100-[096,097,036,126,173,182,245,137,138,025,162,154-157,161,213,122,439,451,467,313,495,183,226,228,412,413,378,387-388,077,086,122]

# activate conda env #SBATCH --cpus-per-task=28
source /mbz/users/fan.zhou/miniconda3/bin/activate
conda activate matheval

export model_name="tinyllama_1_1B_cpt/2017_2024_post_extraction_v2_new_run_stage2_math_scoring_finemath_score_090_cpt_55B"

# get all model ckpt absolute paths
hf_ckpt_dir=~/backup/storage/finemath/hf/${model_name}

# Create a log directory for debugging
mkdir -p ~/backup/finemath-eval/eval_logs/${model_name}
log_dir=~/backup/finemath-eval/eval_logs/${model_name}

# Get a list of model checkpoints and create a log file
ls -1 ${hf_ckpt_dir} > ${log_dir}/all_checkpoints.log
echo "Total models found: $(wc -l ${log_dir}/all_checkpoints.log)" > ${log_dir}/summary.log

cd ~/backup/finemath-eval/

# Get all model checkpoints as absolute paths in array
model_paths=()
for path in $(ls ${hf_ckpt_dir}); do
    model_paths+=(${hf_ckpt_dir}/${path})
done

# Export variables for all nodes to access
export N_MODELS=${#model_paths[@]}
export MODEL_PATHS=(${model_paths[@]})

echo "Found ${N_MODELS} models to evaluate" >> ${log_dir}/summary.log
echo "Model paths:" >> ${log_dir}/model_paths.log
printf "%s\n" "${MODEL_PATHS[@]}" >> ${log_dir}/model_paths.log

# Parallel evaluation command for each node
cmd='
# Receive paths as command line arguments
model_paths=("$@")  
node_id=$SLURM_NODEID
total_nodes=$SLURM_NNODES
log_dir=~/backup/finemath-eval/eval_logs/${model_name}

# Create a log file for this node
node_log=${log_dir}/node_${node_id}.log
echo "Node ${node_id} starting processing" > ${node_log}

# Improved model distribution algorithm - assign models evenly across nodes
model_paths_for_node=()
for ((i=node_id; i<$N_MODELS; i=i+total_nodes)); do
    model_paths_for_node+=(${MODEL_PATHS[$i]})
done

# Log what models this node will process
echo "Node ${node_id} will process ${#model_paths_for_node[@]} models:" >> ${node_log}
printf "%s\n" "${model_paths_for_node[@]}" >> ${node_log}

# Execute evaluation script if we have models to process
if [ ${#model_paths_for_node[@]} -gt 0 ]; then
    echo "Starting evaluation on node ${node_id}" >> ${node_log}
    bash scripts/en_math_cot_eval.sh "${model_paths_for_node[@]}" >> ${node_log} 2>&1
    echo "Evaluation complete on node ${node_id}" >> ${node_log}
else
    echo "No models to process on node ${node_id}" >> ${node_log}
fi
'

# Run the distributed evaluation
srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 bash -c "$cmd" -- "${MODEL_PATHS[@]}"

# Summarize results after all evaluations complete
python summarize_results.py \
    --dirname outputs/hf/${model_name} \
    --summarize_dir perf_results/hf/${model_name}

# Create a final summary log
echo "Evaluation completed at $(date)" >> ${log_dir}/summary.log
ls -la outputs/hf/${model_name} >> ${log_dir}/summary.log
echo "Results summary generated in perf_results/hf/${model_name}" >> ${log_dir}/summary.log