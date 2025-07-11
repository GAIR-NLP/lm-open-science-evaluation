cd /inspire/hdd/global_user/liupengfei-24025/rzfan/finemath-eval
export PATH="/inspire/hdd/global_user/liupengfei-24025/rzfan/miniconda3/bin:$PATH"
source activate finemath_eval

export VLLM_HOST_IP="127.0.0.1"

# configuration args
# default model ckpts will be in the first arg, send as a list
# e.g., bash eval.sh ${model_paths_for_node[@]}
model_path=/inspire/hdd/global_user/liupengfei-24025/rzfan/models/science_sft/qwen2.5-7B/textbook_reasoing_final_76w_v3_distill_cot_filtering_qa_decontamination_difficulty_reasoning_v3_distill.lr5e-6.bs512/checkpoint-3813
tokenizer_path=${model_path}
overwrite=true
model_size="7b"
use_vllm=true
no_markup_question=true
test_conf=configs/en_science_sft_configs.json
prompt_format=few_shot
expname=eval_science_sft

# NOTE: output dir should better be a multi-level dir
# I want to get like: finemath/hf/tinyllama_1_1B_cpt/CC-MAIN-2024-26-mathrecall_iter1_v0_w_nltk_normalization_2000k_060_fw_edu_df_15B/1.0B
last_3_dirs=$(basename $(dirname $(dirname $(dirname ${model_path}))))
last_2_dirs=$(basename $(dirname $(dirname ${model_path})))
last_1_dirs=$(basename $(dirname ${model_path}))
last_0_dirs=$(basename ${model_path})
output_dir=outputs/${last_3_dirs}/${last_2_dirs}/${last_1_dirs}/${last_0_dirs}

# other eval execution args
n_gpus=8
temperature=0
n_repeats=1

# to avoid deadlocks
export TOKENIZERS_PARALLELISM=false

# submit eval jobs
/inspire/hdd/global_user/liupengfei-24025/rzfan/miniconda3/envs/finemath_eval/bin/python submit_eval_jobs.py \
    --n-gpus $n_gpus \
    --temperature $temperature \
    --n-repeats $n_repeats \
    --output-dir $output_dir \
    --model-path $model_path \
    --tokenizer-path $tokenizer_path \
    --model-size $model_size \
    --overwrite $overwrite \
    --no-markup-question $no_markup_question \
    --use-vllm $use_vllm \
    --test-conf $test_conf \
    --prompt_format $prompt_format \
    --expname $expname
# wait until the jobs are done
wait
# break
# exit