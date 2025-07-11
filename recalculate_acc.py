import json
import os
from data_processing.answer_extraction import *
from eval.eval_script import *

model_list = [
    "outputs/liupengfei-24025/rzfan/models/Qwen2.5-7B-Instruct",
    "outputs/science_sft/qwen2.5-7B/natural_reasoning.lr5e-6.bs128/checkpoint-6714",
    "outputs/science_sft/qwen2.5-7B/scp116k_reasoning.lr5e-6.bs32/checkpoint-25704",
    "outputs/science_sft/qwen2.5-7B/nemotro_science.lr5e-6.bs128/checkpoint-16617",
    "outputs/science_sft/qwen2.5-7B/textbooks_reasoning_distill_llama3.3_70b.lr5e-6.bs512/checkpoint-3774",
    "outputs/science_sft/qwen2.5-7B/textbooks_reasoning_with_document_distill_v3_38w.lr5e-6.bs256/checkpoint-4551",
    "outputs/science_sft/qwen2.5-7B/textbooks_reasoning_with_document_distill_v3_fultering_qa_36w.lr5e-6.bs256/checkpoint-4320"
]

benchmark_list = [
    "olympic-arena-astronomy",
    "olympic-arena-biology",
    "olympic-arena-chemistry",
    "olympic-arena-geography",
    "olympic-arena-math",
    "olympic-arena-physics"
]

for model in model_list:
    for benchmark in benchmark_list:
        print(model)
        print(benchmark)
        prediction_path = os.path.join(model, benchmark, "infer_logs/sft/samples/predictions.json")
        
        with open(prediction_path, "r", encoding="utf-8") as fp:
            prediction = json.load(fp)
        acc_num = 0
        for pre in prediction:
            pre["prediction"] = extract_olympic_arena_sft_answer(pre)
            res = eval_olympic_arena(pre)
            if res:
                acc_num += 1
        print(acc_num / len(prediction) * 100)