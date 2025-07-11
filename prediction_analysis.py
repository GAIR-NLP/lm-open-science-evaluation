import json
import random
import sys

# path = "/mbz/users/fan.zhou/backup/finemath-eval/outputs/zengzhi.wang/storage/ckpts/TinyLlama-1.1B-intermediate-step-1431k-3T/agieval-gaokao-mathqa-cot-test/infer_logs/cot/samples/predictions.json"

if len(sys.argv) < 2:
    print("Usage: python script.py <path_to_json>")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, "r") as f:
    data = json.load(f)

idx = random.randint(0, len(data))
item = data[idx]

for key in item:
    print(f">>>>>>>>>>>>>>>>>>>>>>>{key}")
    print(item[key])