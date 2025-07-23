# Language Model Open Science Evaluation

## Introduction

The **Language Model Open Science Evaluation** is a comprehensive evaluation framework originally developed for evaluating mathematical reasoning abilities of language models after continued pre-training. Initially focused on mathematics, it has since been expanded to cover multiple scientific disciplines and now supports evaluation of both base and instruction-tuned LLMs. Used internally within [GAIR](https://plms.ai/index.html), this repository provides the complete codebase to faithfully reproduce evaluation results from our recent research papers in mathematical and scientific reasoning.

Our evaluation system supports reproducible experiments from the following research works:

- **OctoThinker**: Mid-training Incentivizes Reinforcement Learning Scaling ([arXiv:2506.20512](https://arxiv.org/abs/2506.20512))

- **MegaScience**: Pushing the Frontiers of Post-Training Datasets for Science Reasoning ([arXiv:2507.16812](https://arxiv.org/abs/2507.16812))


This evaluation system can also be applied to our previous pre-training research work:

- Programming Every Example: Lifting Pre-training Data Quality Like Experts at Scale ([arXiv:2409.17115](https://arxiv.org/abs/2409.17115))

Although, in that work, we used a different evaluation infrastructure: [GAIR-NLP/math-evaluation-harness](https://github.com/GAIR-NLP/math-evaluation-harness)



This codebase builds upon and incorporates valuable features from [DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math) by DeepSeek AI.

## Setup
Clone the repository and install the required dependencies. We recommend using a virtual environment with Python 3.10 or higher:
```bash
git clone https://github.com/GAIR-NLP/lm-open-science-evaluation.git
cd lm-open-science-evaluation
conda create -n lmose python=3.10
conda activate lmose
pip install -r requirements.txt
# for flash-attn, you may need to install it manually
pip install flash-attn --no-build-isolation
```

## Evaluation

### Configuration Setup

Before running evaluations, you need to create and configure benchmark settings in the `configs` directory. Each item in the configuration represents a benchmark to be evaluated.

#### Configuration Format

Create a configuration file in the `configs` directory with the following structure:

```json
{
    "benchmark-name": {
        "test_path": "path/to/test/dataset.jsonl",
        "language": "en",
        "tasks": ["cot"],
        "process_fn": "process_function_name",
        "answer_extraction_fn": "extraction_function_name", 
        "eval_fn": "evaluation_function_name",
        "few_shot_prompt": "PromptClassName"
    }
}
```

#### Configuration Parameters

- **`test_path`**: Path to the test dataset file (typically in JSONL or JSON format)
- **`language`**: Language of the benchmark (`"en"` for English, `"zh"` for Chinese)
- **`tasks`**: List of evaluation tasks to run:
  - `"cot"`: Chain-of-thought evaluation for base models
  - `"pal"`: Program-aided language evaluation for base models  
  - `"sft"`: Evaluation for instruction-tuned models
- **`process_fn`**: Function name for preprocessing the test dataset. Find the appropriate function in `data_processing/process_utils.py` and set the function name here
- **`answer_extraction_fn`**: Function name for extracting answers from model responses. Find the corresponding function in `data_processing/answer_extraction.py`
- **`eval_fn`**: Function name for evaluating extracted answers against ground truth. Find the appropriate function in `eval/eval_script.py`
- **`few_shot_prompt`**: Prompt template for evaluation. Choose from existing prompts in the `few_shot_prompts` directory or create new ones. Available options include few-shot, zero-shot, or chain-of-thought prompts. If creating new prompts, remember to add them to `few_shot_prompts/__init__.py`

#### Example Configuration

```json
{
    "gsm8k-cot": {
        "test_path": "datasets/gsm8k/test.jsonl",
        "language": "en",
        "tasks": ["cot"],
        "process_fn": "process_gsm8k_test",
        "answer_extraction_fn": "extract_gsm_few_shot_cot_answer",
        "eval_fn": "eval_last_single_answer",
        "few_shot_prompt": "CoTGSMPrompt"
    }
}
```

### Running Evaluations

After configuring your benchmarks, create evaluation scripts in the `scripts` directory. Set the appropriate model path and GPU configuration in your script, then execute the evaluation.

The evaluation system will automatically process the configured benchmarks according to your specifications and generate comprehensive results.

## Specific Evaluation Suites


### OctoThinker Evaluations (CPT Usage)


Note that the your_model_folder_path should be like:


```
$ ls your_model_folder_path
1B/  2B/  3B/  4B/  5B/  6B/  7B/  8B/  9B/ 10B/
```

Suppose you have 8 GPU nodes, with 8 GPU devices per node, and you plan to evaluate these checkpoints in parallel. In your SLURM or Kubernetes scripts, you will distribute the checkpoints across the 8 nodes. In other words, each node will be assigned a subset of checkpoint paths, such as one or two checkpoints per node.


<details>
<summary>An Example Slurm Script</summary>

```
#!/bin/bash
#SBATCH --job-name=cpt_eval
#SBATCH --output=logs/eval.%J.log
#SBATCH --partition=xxx
#SBATCH --error=logs/eval.%J.log
#SBATCH --time=50:00:00
#SBATCH --nodes=8
#SBATCH --mem=0
#SBATCH --ntasks-per-node=8
#SBATCH --gres=gpu:8
#SBATCH --exclusive

cd lm-open-science-evaluation/
source xxx/miniconda3/bin/activate
conda activate matheval


ckpt_dir=llama_3_2_1B_nanotron_cpt/megamath-web-pro/bs2_lr5e-5_seq8k_15B_dp256
hf_ckpt_dir=your_storage_path/hf/${ckpt_dir}


export NNODES=$SLURM_NNODES

model_paths=()

for path in $(ls ${hf_ckpt_dir}); do
    model_paths+=(${hf_ckpt_dir}/${path})
done
length=${#model_paths[@]}
export N_MODELS=$length
export MODEL_PATHS=(${model_paths[@]})
echo "model paths: ${MODEL_PATHS[@]}"



# parallel eval all models on multi-nodes
cmd='
model_paths=("$@")  # Receive paths as command line arguments
node_id=$SLURM_NODEID
total_nodes=$SLURM_NNODES

# if SLURM_NODEID >= N_MODELS, then exit
if [ $node_id -ge $N_MODELS ]; then
    total_nodes=$N_MODELS
    exit 0
fi

# function to get the n-th model path for the current node
get_path_for_node() {
    local n=$1
    echo ${model_paths[$((n * total_nodes + node_id))]}
}

# generate the list of model paths for the current node
model_paths_for_node=()
n=0
while true; do
    path=$(get_path_for_node $n)
    echo "path: $path"
    if [ -n "$path" ]; then
        model_paths_for_node+=($path)
    fi
    n=$((n + 1))
    if [ $((n * total_nodes + node_id + 1)) -ge $N_MODELS ]; then
        break
    fi
done

# verbose
echo "model_paths_for_node: ${model_paths_for_node[@]}"
bash scripts/en_math_cot_eval.sh ${model_paths_for_node[@]}
'

srun --ntasks=$NNODES --ntasks-per-node=1 bash -c "$cmd" -- "${MODEL_PATHS[@]}"

cd lm-open-science-evaluation
python summarize_results.py \
    --dirname outputs/${ckpt_dir} \
    --summarize_dir perf_results/${ckpt_dir}
```

</details>


### MegaScience Evaluations (SFT Usage)

To reproduce the results in the [MegaScience paper](https://arxiv.org/abs/2507.16812):

```bash
bash scripts/eval_science.sh <model_path>
```


## Evaluation Output

The evaluation results are stored in the specified `outputs` directory with a structured file organization for each task and model.

### Output Directory Structure

The output follows a hierarchical directory structure:
```
outputs/
└── model_dir_path_3/
    └── model_dir_path_2/
        └── model_dir_path_1/
            └── benchmark_name/
                └── samples/
                    ├── metrics.json
                    └── predictions.json
```

### Output Files

#### `metrics.json`
Contains the final evaluation metrics for the specific model on the benchmark, including accuracy scores and other performance indicators.

#### `predictions.json`
Contains detailed predictions and responses in the following format:

```json
{
    "dataset": "benchmark_name",
    "id": "unique_sample_id",
    "messages": [
        {
            "role": "user",
            "content": "formatted_question_with_prompt"
        },
        {
            "role": "assistant", 
            "content": ""
        }
    ],
    "answer": "ground_truth_answer",
    "reference": "reference_solution",
    "prompt": "question_within_prompt_template",
    "model_output": "raw_model_response",
    "prediction": [
        "extracted_answer_from_model_output"
    ],
    "accuracy": "sample_level_accuracy_score"
}
```

### Field Descriptions

- **`dataset`**: Name of the benchmark being evaluated
- **`id`**: Unique identifier for each test sample
- **`messages`**: Chat format containing the user question and assistant response placeholder
- **`answer`**: Ground truth answer from the dataset
- **`reference`**: Reference solution or explanation (if available)
- **`prompt`**: The complete formatted prompt sent to the model
- **`model_output`**: Raw response generated by the model
- **`prediction`**: Extracted answer(s) from the model output using the specified extraction function
- **`accuracy`**: Binary accuracy score (1.0 for correct, 0.0 for incorrect) for this specific sample

This structured output format enables detailed analysis of model performance, error patterns, and facilitates further research and debugging.

## 🥳 Citation

If you find this work useful, please cite:

```
@article{wang2025octothinker,
  title={OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling},
  author={Wang, Zengzhi and Zhou, Fan and Li, Xuefeng and Liu, Pengfei},
  year={2025},
  journal={arXiv preprint arXiv:2506.20512},
  url={https://arxiv.org/abs/2506.20512}
}
```

```
@article{fan2025megascience,
  title={MegaScience: Pushing the Frontiers of Post-Training Datasets for Science Reasoning},
  author={Fan, Run-Ze and Wang, Zengzhi and Liu, Pengfei},
  year={2025},
  journal={arXiv preprint arXiv:2507.16812},
  url={https://arxiv.org/abs/2507.16812}
}
```
