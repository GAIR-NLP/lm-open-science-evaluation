from datasets import load_dataset
import json

test_set = []
ds = load_dataset("TIGER-Lab/MMLU-Pro")["test"]
for d in ds:
    test_set.append(d)
    
print(len(test_set))

with open(f"test.json", "w") as fp:
    fp.write(json.dumps(test_set, indent=4, ensure_ascii=False))