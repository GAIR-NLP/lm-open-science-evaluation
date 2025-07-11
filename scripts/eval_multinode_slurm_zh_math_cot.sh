#!/bin/bash
#SBATCH --job-name=finemath_eval
#SBATCH --output=/mbz/users/fan.zhou/backup/slurm/job.%J.log
#SBATCH --partition=mbzuai
#SBATCH --error=/mbz/users/fan.zhou/backup/slurm/job.%J.err
#SBATCH --time=50:00:00
#SBATCH --nodes=25
#SBATCH --ntasks-per-node=8
#SBATCH --gres=gpu:8
#SBATCH --exclusive
#SBATCH --exclude=g42-odin-h100-[001-100,096,097,036,126,173,182,245,137,138,025,162]



# activate conda env #SBATCH --cpus-per-task=28
source /mbz/users/fan.zhou/miniconda3/bin/activate
conda activate matheval


export model_name=InfiMM-WebMath-Edu-zh_exact_dedup_25B

export NNODES=25

# get all model ckpt absolute paths
hf_ckpt_dir=~/backup/storage/finemath/hf/tinyllama_1_1B_cpt/${model_name}
model_paths=()

for path in $(ls ${hf_ckpt_dir}); do
    model_paths+=(${hf_ckpt_dir}/${path})
done
length=${#model_paths[@]}
export N_MODELS=$length
export MODEL_PATHS=(${model_paths[@]})
echo "model paths: ${MODEL_PATHS[@]}"




# parallel eval all models on multi-nodes
cmd='
model_paths=("$@")  # Receive paths as command line arguments
node_id=$SLURM_NODEID
total_nodes=$SLURM_NNODES

# if SLURN_NODEID >= N_MODELS, then exit
if [ $node_id -ge $N_MODELS ]; then
    total_nodes=$N_MODELS
    exit 0
fi

# function to get the n-th model path for the current node
get_path_for_node() {
    local n=$1
    echo ${model_paths[$((n * total_nodes + node_id))]}
}

# generate the list of model paths for the current node
model_paths_for_node=()
n=0
while true; do
    path=$(get_path_for_node $n)
    echo "path: $path"
    if [ -n "$path" ]; then
        model_paths_for_node+=($path)
    fi
    n=$((n + 1))
    if [ $((n * total_nodes + node_id + 1)) -ge $N_MODELS ]; then
        break
    fi
done

# verbose
echo "model_paths_for_node: ${model_paths_for_node[@]}"
bash scripts/zh_math_cot_eval.sh ${model_paths_for_node[@]}
'

# srun --ntasks=$NNODES --ntasks-per-node=1 bash -c "$cmd"
srun --ntasks=$NNODES --ntasks-per-node=1 bash -c "$cmd" _ "${MODEL_PATHS[@]}"


python summarize_results.py \
    --dirname outputs/hf/tinyllama_1_1B_cpt/${model_name} \
    --summarize_dir perf_results/hf/tinyllama_1_1B_cpt/${model_name}