

prefix=/mbz/users/fan.zhou/backup/storage/finemath/hf

META_DIR=llama_3_1_8B_nanotron_cpt/megamath

for ckpt_dir in  ${META_DIR}/decay_code_035_mixture_bs4M_cosine_lr1e-6_seq8k_10B_dp8_tp8
do
    for size in 8.0B
    do 
        echo "Resuming $size"
        # bash scripts/zh_math_cot_eval.sh ${prefix}/${ckpt_dir}/${size} 4
        bash scripts/en_math_cot_pot_eval.sh ${prefix}/${ckpt_dir}/${size} 
    done

    python summarize_results.py \
        --dirname outputs/${ckpt_dir} \
        --summarize_dir perf_results/${ckpt_dir}
done