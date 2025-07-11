export MKL_THREADING_LAYER=GNU
export MKL_THREADING_LAYER=INTEL
export MKL_SERVICE_FORCE_INTEL=1


MODEL_NAME_OR_PATH=$1

# last_dirs=$(scripts/get_last_n_dirs.sh ${MODEL_NAME_OR_PATH} 2)

# echo $last_dirs


last_3_dirs=$(basename $(dirname $(dirname $(dirname ${MODEL_NAME_OR_PATH}))))
last_2_dirs=$(basename $(dirname $(dirname ${MODEL_NAME_OR_PATH})))
last_1_dirs=$(basename $(dirname ${MODEL_NAME_OR_PATH}))
last_0_dirs=$(basename ${MODEL_NAME_OR_PATH})

OUTPUT_DIR=outputs/${last_3_dirs}/${last_2_dirs}/${last_1_dirs}/${last_0_dirs}


echo $OUTPUT_DIR

python submit_eval_jobs.py --n-gpus 8 \
    --output-dir ${OUTPUT_DIR} \
    --model-path ${MODEL_NAME_OR_PATH} \
    --tokenizer-path ${MODEL_NAME_OR_PATH} \
    --model-size 1b \
    --use-vllm True \
    --test-conf configs/en_math_cot_few_shot_test_configs.json \
    --prompt_format few_shot \
    --overwrite False \
    --no-markup-question True \
    --expname tinyllama-base