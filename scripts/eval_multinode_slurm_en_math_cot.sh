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

# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_5gram_11buckets_10hashes_dedup_v040_090_55B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_5gram_9buckets_12hashes_dedup_v040_090_55B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_5gram_9buckets_13hashes_dedup_v040_090_55B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_5gram_11buckets_11hashes_dedup_v040_090_55B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_5gram_14buckets_9hashes_dedup_v040_090_55B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_5gram_11buckets_10hashes_dedup_v040_url_dedup_090_55B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_5gram_b14_r8_dedup_v040_url_dedup_090_55B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_5gram_b14_r8_dedup_v040_090_55B"
# export model_name="CC-MAIN-2015-all_050_seperate_exact_dedup_minhash_5gram_11buckets_10hashes_dedup_v040_090_55B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_5gram_b14_r8_dedup_v040_wo_number_norm_090_55B"
# export model_name="CC-MAIN-2015-all_050_seperate_exact_dedup_minhash_5gram_11buckets_10hashes_dedup_v040_url_dedup_090_55B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_13gram_11buckets_10hashes_dedup_v040_090_55B"
# export model_name="CC-MAIN-2015-all_050_seperate_exact_dedup_minhash_5gram_11buckets_10hashes_dedup_v040_wo_number_norm_090_55B"


# export model_name="CC-MAIN-2024-10_dedup_post_extraction_trafilatura_text_combined_score_090_15B"
# export model_name="CC-MAIN-2024-10_dedup_post_extraction_trafilatura_text_resiliparse_score_090_15B"
# export model_name="CC-MAIN-2024-10_dedup_post_extraction_trafilatura_text_trafilatura_score_090_15B"
# export model_name="CC-MAIN-2024-10_dedup_post_extraction_trafilatura_text_min_score_080_15B"
# export model_name="CC-MAIN-2014-all_050_seperate_exact_dedup_minhash_9gram_11buckets_10hashes_dedup_v040_090_55B"

# export model_name="CC-MAIN-2024-10_dedup_post_extraction_resiliparse_text_combined_score_080_15B"
# export model_name="CC-MAIN-2024-10_dedup_post_extraction_resiliparse_text_combined_score_090_15B"

# export model_name="CC-MAIN-2024-10_dedup_post_extraction_trafilatura_text_combined_score_060_edu_df_15B"

# export model_name="CC-MAIN-2024-10_dedup_wo_number_norm_post_extraction_trafilatura_text_combined_score_080_15B"
# export model_name="CC-MAIN-2024-10_dedup_wo_number_norm_post_extraction_trafilatura_text_combined_score_090_15B"
# export model_name="CC-MAIN-2024-10_dedup_quality_filter_post_extraction_trafilatura_text_combined_score_090_15B"
# export model_name="CC-MAIN-2024-10_dedup_quality_filter_post_extraction_trafilatura_text_combined_score_080_15B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_v2_trafilatura_text_combined_score_090_15B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-all_dedup_post_extraction_trafilatura_text_combined_score_080_55B"
# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-all_dedup_post_extraction_trafilatura_text_combined_score_090_55B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-all_dedup_post_extraction_v2_trafilatura_text_combined_score_090_55B"
# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-all_dedup_post_extraction_v2_trafilatura_text_combined_score_080_55B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_v2_new_trafilatura_text_combined_score_080_15B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-all_dedup_post_extraction_v2_new_trafilatura_text_combined_score_090_55B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_v2_new_trafilatura_text_combined_score_090_15B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-all_dedup_post_extraction_v2_new_trafilatura_text_combined_score_080_55B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_stage2_math_scoring_threshold3_mix_infimmwebmath_random_cc_4M_090_15B"
# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_stage2_math_scoring_threshold3_mix_infimmwebmath_random_cc_4M_080_15B"
# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_stage2_math_scoring_threshold3_mix_infimmwebmath_random_cc_4M_095_15B"


# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_stage2_math_scoring_threshold4_mix_infimmwebmath_edu_random_cc_4M_080_15B"
# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_stage2_math_scoring_threshold4_mix_infimmwebmath_edu_random_cc_4M_090_15B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_stage2_math_scoring_threshold3_040_15B"
# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_stage2_math_scoring_threshold4_030_15B"
# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_stage2_math_scoring_threshold4_040_15B"

# export model_name="tinyllama_1_1B_cpt/CC-MAIN-2024-10_dedup_post_extraction_trafilature_text_combined_score_090_sent_dedup_15B"

# export model_name="tinyllama_1_1B_cpt/all_year_dedup_post_extraction_stage2_math_scoring_threshold4_040_wo_dump_2022_33_cpt_250B"

cd ~/backup/finemath-eval/

# export model_name="tinyllama_1_1B_cpt/all_year_dedup_post_extraction_v2_new_run_stage2_math_scoring_threshold4_090_cpt_250B"

# export model_name="tinyllama_1_1B_cpt/2018_all_post_extraction_v2_new_run_stage2_math_scoring_finemath_score_090_cpt_5B"
# export model_name="tinyllama_1_1B_cpt/2018_all_dedup_post_extraction_v2_new_run_stage2_math_scoring_threshold4_090_5B"

# export model_name="tinyllama_1_1B_cpt/rt09_s204_fast09_2014"

# export model_name="tinyllama_1_1B_cpt/all_year_dedup_post_extraction_v2_new_run_stage2_math_scoring_threshold4_040_wo_dump_2022_33_cpt_250B"

export model_name="tinyllama_1_1B_cpt/2017_2024_post_extraction_v2_new_run_stage2_math_scoring_finemath_score_090_cpt_55B"

# get all model ckpt absolute paths
hf_ckpt_dir=~/backup/storage/finemath/hf/${model_name}

ls ${hf_ckpt_dir}



# export model_name="llama_3_2_1B_nanotron_cpt/bs4_seq4k_15B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/bs4_lr5e-5_seq4k_15B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/bs4_lr1e-5_seq4k_15B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/openwebmath/bs4_lr3e-5_seq4k_15B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/openwebmath/bs2_lr5e-5_seq8k_15B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/finemath-4plus/bs4_lr5e-5_seq4k_15B_dp256"

# export model_name="llama_3_2_1B_nanotron_cpt/open-web-math-pro/bs4_lr5e-5_seq4k_15B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/infiwebmath-4plus/bs4_lr5e-5_seq4k_15B_dp256"


# export model_name="llama_3_2_1B_nanotron_cpt/InfiMM-WebMath-En-Text/bs4_lr5e-5_seq4k_55B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/InfiMM-WebMath-Edu/bs4_lr5e-5_seq4k_55B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/finemath-3plus/bs4_lr5e-5_seq4k_55B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/infiwebmath-3plus/bs4_lr5e-5_seq4k_55B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/InfiMM-WebMath-En-Text/bs4_lr5e-5_seq4k_55B_dp256_fix_bug"

# export model_name="llama_3_2_1B_nanotron_cpt/finemath-4plus-infimmwebmath-4plus/bs4_lr5e-5_seq4k_55B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/finemath-4plus-infimmwebmath-4plus-owm-pro/bs4_lr5e-5_seq4k_55B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/finemath-3plus-infimmwebmath-3plus/bs4_lr5e-5_seq4k_55B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/finemath-3plus-edu-infimmwebmath-3plus-edu/bs4_lr5e-5_seq4k_55B_dp256"

# export model_name="llama_3_2_1B_nanotron_cpt/finemath-4plus-infimmwebmath-4plus-owm-pro/221_mixture_bs4_lr5e-5_seq4k_55B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/finemath-4plus-infimmwebmath-4plus-owm-pro/332_mixture_bs4_lr5e-5_seq4k_55B_dp256"
# export model_name="llama_3_2_1B_nanotron_cpt/finemath-3plus-edu-infimmwebmath-3plus-edu-owm-pro/bs4_lr5e-5_seq4k_55B_dp256"

# export model_name="llama_3_2_3B_nanotron_cpt/finemath-4plus-infimmwebmath-4plus/bs8_lr5e-5_seq4k_55B_dp128"



# export model_name="llama_3_2_1B_nanotron_cpt/InfiMM-WebMath-En-Text-finemath-3plus/bs2_lr5e-5_seq8k_100B_dp512"
# export model_name="llama_3_2_1B_nanotron_cpt/InfiMM-WebMath-En-Text-finemath-3plus/bs4_lr5e-5_seq4k_100B_dp512"
# export model_name="llama_3_2_1B_nanotron_cpt/InfiMM-WebMath-En-Text-finemath-3plus-dedup/bs4_lr5e-5_seq4k_100B_dp512"


# hf_ckpt_dir=~/backup/storage/finemath/hf/${model_name}

export NNODES=${SLURM_NNODES}

model_paths=()

for path in $(ls ${hf_ckpt_dir}); do
    model_paths+=(${hf_ckpt_dir}/${path})
done
length=${#model_paths[@]}
export N_MODELS=$length
export MODEL_PATHS=(${model_paths[@]})
export N_MODELS=${#MODEL_PATHS[@]}
echo "model paths: ${MODEL_PATHS[@]}"
echo "N_MODELS: $N_MODELS"




# parallel eval all models on multi-nodes
cmd='
model_paths=("$@")  # Receive paths as command line arguments
node_id=$SLURM_NODEID
total_nodes=$SLURM_NNODES

# if SLURM_NODEID >= N_MODELS, then exit
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
bash scripts/en_math_cot_eval.sh ${model_paths_for_node[@]}
'

# srun --ntasks=$NNODES --ntasks-per-node=1 bash -c "$cmd"
# srun --ntasks=$NNODES --ntasks-per-node=1 bash -c "$cmd" _ "${MODEL_PATHS[@]}"
srun --ntasks=$NNODES --ntasks-per-node=1 bash -c "$cmd" -- "${MODEL_PATHS[@]}"

python summarize_results.py \
    --dirname outputs/hf/${model_name} \
    --summarize_dir perf_results/hf/${model_name}

# python summarize_results.py \
#     --dirname outputs/${model_name} \
#     --summarize_dir perf_results/hf/${model_name}