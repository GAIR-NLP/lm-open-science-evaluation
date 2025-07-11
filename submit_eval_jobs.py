import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    # Configuration options
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--model-path", type=str, required=True)
    parser.add_argument("--tokenizer-path", type=str, required=True)
    parser.add_argument("--model-size", type=str, required=True)
    parser.add_argument("--overwrite", type=str, required=True)
    parser.add_argument("--use-vllm", type=str, required=True)
    parser.add_argument("--no-markup-question",type=str, required=True)
    parser.add_argument("--test-conf", type=str, required=True)
    parser.add_argument("--prompt_format", type=str, required=True)
    parser.add_argument("--expname", type=str, required=True)

    # Execution options
    parser.add_argument("--n-repeats", type=int ,default=1)
    parser.add_argument("--temperature", type=float, default=0)
    parser.add_argument("--n-gpus", type=int, default=8)
    args = parser.parse_args()

    # pack configuration into json
    conf = {
        'output-dir': args.output_dir,
        'model-path': args.model_path,
        'tokenizer-path': args.tokenizer_path,
        'model-size': args.model_size,
        'overwrite': True if args.overwrite.lower() == 'true' else False,
        'use-vllm': True if args.use_vllm.lower() == 'true' else False,
        'no-markup-question': True if args.no_markup_question.lower() == 'true' else False,
        'test-conf': args.test_conf,
        'prompt_format': args.prompt_format,
        'expname': args.expname,
    }

    cmd = "python run_subset_parallel.py"
    for key, val in conf.items():
        if key == 'expname':
            continue
        if isinstance(val, str):
            cmd += f" --{key} {val}"
        elif val:
            cmd += f" --{key}"
    cmd += f" --test-conf {conf['test-conf']}"
    cmd += f" --n-repeats {args.n_repeats}"
    cmd += f" --temperature {args.temperature}"
    cmd += f" --ngpus {args.n_gpus}"
    cmd += f" --rank {0}"
    print(cmd, flush=True)
    os.system(cmd)

if __name__ == '__main__':
    main()
