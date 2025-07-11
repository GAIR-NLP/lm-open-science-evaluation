

prefix=/mbz/users/fan.zhou/backup/storage/finemath/hf
# ckpt_dir=llama_3_2_1B_nanotron_cpt/analysis/megamath-web-pro/bs2_lr5e-5_seq8k_20B_dp256

# ckpt_dir=llama_3_1_8B_nanotron_cpt/megamath/decay_shortqa_020_mixture_bs4M_constant_lr3e-6_seq8k_10B_dp16_tp8
# ckpt_dir=llama_3_1_8B_nanotron_cpt/megamath/decay_shortqa_020_mixture_bs4M_lr0_seq8k_10B_dp16_tp8
# ckpt_dir1=decay_shortqa_020_mixture_bs4M_constant_lr2e-6_seq8k_10B_dp16_tp8
# ckpt_dir2=decay_shortqa_020_mixture_bs4M_constant_lr3e-6_seq8k_10B_dp16_tp8

META_DIR=llama_3_1_8B_nanotron_cpt/megamath

for ckpt_dir in  ${META_DIR}/decay_longcotqa_openr1_qwq_040_mixture_bs4M_cosine_lr1e-6_seq8k_20B_dp16_tp8
do
    for size in 13.0B 17.0B 15.0B
    do 
        echo "Resuming $size"
        # bash scripts/zh_math_cot_eval.sh ${prefix}/${ckpt_dir}/${size} 4
        bash scripts/en_math_cot_eval.sh ${prefix}/${ckpt_dir}/${size} 
    done

    python summarize_results.py \
        --dirname outputs/${ckpt_dir} \
        --summarize_dir perf_results/${ckpt_dir}
done

# export ckpt_dir=llama_3_1_8B_nanotron_cpt/megamath/decay_code_035_mixture_bs4M_cosine_lr1e-6_seq8k_10B_dp8_tp8