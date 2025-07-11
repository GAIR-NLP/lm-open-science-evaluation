from datasets import load_dataset
import json
import huggingface_hub 
huggingface_hub.login("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")

test_set = []
ds = load_dataset("Idavidrein/gpqa", "gpqa_main")["train"]
for d in ds:
    test_set.append(d)
    
print(len(test_set))

with open(f"datasets/gpqa/gpqa_main.json", "w") as fp:
    fp.write(json.dumps(test_set, indent=4, ensure_ascii=False))