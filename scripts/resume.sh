



model_name=$1


prefix_dir=/mbz/users/fan.zhou/backup/storage/finemath/hf/tinyllama_1_1B_cpt

bash scripts/en_math_cot_eval.sh ${prefix_dir}/${model_name}

