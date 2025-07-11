# configuration args
# set default model path as well
model_dir=${1:-~/backup/storage/ckpts/Llama-3.1-8B-hf/}
model_path=${1:-~/backup/storage/ckpts/Llama-3.1-8B-hf/}
# for model_path in ${model_dir}/*; do
tokenizer_path=${model_path}
model_size=${2:-7b}
overwrite=true  
use_vllm=true
no_markup_question=true
test_conf=configs/dev_few_shot_test_configs.json
prompt_format=few_shot
expname=eval-finemath-template

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
python submit_eval_jobs.py \
    --n-gpus $n_gpus \
    --temperature $temperature \
    --n-repeats $n_repeats \
    --output-dir $output_dir \
    --model-path $model_path \
    --tokenizer-path $tokenizer_path \
    --model-size $model_size \
    --overwrite $overwrite \
    --use-vllm $use_vllm \
    --no-markup-question $no_markup_question \
    --test-conf $test_conf \
    --prompt_format $prompt_format \
    --expname $expname
# wait until the jobs are done
wait
# break
# exit
# done

wait 10

# aggregate results (without minif2f)
python summarize_results.py \
    --dirname outputs/${last_3_dirs}/${last_2_dirs}/${last_1_dirs} \
    --summarize_dir perf_results/${last_3_dirs}/${last_2_dirs}/${last_1_dirs}
