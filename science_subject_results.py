import json
from tqdm import tqdm
import os


def subject_result(result_path, benchmark, subject_key):
    pediction_path = os.path.join(result_path, benchmark, 'infer_logs', 'sft', 'samples', 'predictions.json')
    with open(pediction_path, 'r', encoding='utf-8') as fp:
        predictions = json.load(fp)
    subject_acc = dict()
    for d in predictions:
        if d[subject_key] not in subject_acc.keys():
            subject_acc[d[subject_key]] = []
        subject_acc[d[subject_key]].append(d['accuracy'])
    print("="*50 + benchmark + "="*50)
    for sub, acc_list in subject_acc.items():
        print(f"{sub}: {sum(acc_list)/len(acc_list)*100}")
    print("="*50 + benchmark + "="*50)
    return
    

def main():
    results_dir_path = "/inspire/hdd/global_user/liupengfei-24025/rzfan/finemath-eval/outputs/science_sft/qwen2.5-7B/nemotro_science.lr5e-6.bs128/checkpoint-16617"
    benchmark_key_dict = {
        # "mmlu": 'subject',
        # 'mmlu_pro': 'category',
        # 'gpqa_diamond': 'subject',
        # 'gpqa_main': 'subject',
        'super_gpqa': 'discipline'
    }
    for bench, key in benchmark_key_dict.items():
        subject_result(results_dir_path, bench, key)

if __name__ == "__main__":
    main()