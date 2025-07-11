# configuration args
model_path=Qwen/Qwen2.5-Math-1.5B
tokenizer_path=Qwen/Qwen2.5-Math-1.5B
model_size=1b
overwrite=true
use_vllm=true
no_markup_question=true
test_conf=configs/few_shot_test_configs.json
prompt_format=few_shot
expname=eval-qwen-2.5-math-1.5b
# NOTE: output dir should better be a multi-level dir
output_dir=outputs/Qwen2.5-Math-1.5B #

# other eval execution args
n_gpus=8
temperature=0
n_repeats=1

# to avoid deadlocks
export TOKENIZERS_PARALLELISM=false

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
# aggregate results (without minif2f)
python summarize_results.py \
    --dirname outputs \
    --summarize_dir perf_results/baselines
