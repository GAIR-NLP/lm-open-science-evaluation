# Open Science Evaluation System (OSES)

## Introduction

The **Open Science Evaluation System (OSES)** is a comprehensive evaluation framework used internally within [GAIR](https://plms.ai/index.html) for evaluating scientific reasoning capabilities in both base and instruction-tuned LLMs. This repository provides the complete codebase to faithfully reproduce evaluation results from our research papers in mathematical and scientific reasoning.

Our evaluation system supports reproducible experiments from the following research works:

- **MegaScience**: Pushing the Frontiers of Post-Training Datasets for Science Reasoning ([Paper]())
- **OctoThinker**: Mid-training Incentivizes Reinforcement Learning Scaling ([arXiv:2506.20512](https://arxiv.org/abs/2506.20512))

This codebase builds upon and incorporates valuable features from [DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math) by DeepSeek AI.

## Setup
Clone the repository and install the required dependencies. We recommend using a virtual environment with Python 3.10 or higher:
```bash
git clone https://github.com/GAIR-NLP/OSES.git
cd OSES
conda create -n oses python=3.10
conda activate oses
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

## Running specific evaluation suites




## Evaluation output
