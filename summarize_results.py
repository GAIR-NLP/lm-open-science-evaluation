import os
import json
import argparse
import pandas as pd
from glob import glob
from copy import deepcopy

def seek_metrics(path):
    if os.path.isdir(path):
        for subpath in glob(os.path.join(path, "*")):
            yield from seek_metrics(subpath)
    else:
        if "metrics.json" in path:
            yield path

def seek_predictions(path):
    if os.path.isdir(path):
        for subpath in glob(os.path.join(path, "*")):
            yield from seek_predictions(subpath)
    else:
        if "predictions.json" in path:
            yield path

def aggregate_metrics(paths):
    result = {}
    total = 0
    for path in paths:
        metric = json.load(open(path, "r"))
        n_samples = metric['n_samples']
        total += n_samples
        for key, val in metric.items():
            if key != 'n_samples':
                result[key] = result.get(key, 0) + val * n_samples
    for key, val in result.items():
        result[key] = val / total
    result['n_samples'] = total
    return result

def aggregate_predictions(paths):
    data = []
    for path in paths:
        try:
            data.extend(json.load(open(path, "r")))
        except:
            print(path, flush=True)
            continue
    return data

style_hub = [
    {
        'marker': '*',
        'markerfacecolor': '#b5dfff', #'#FFB3BA',  # 浅粉红
        'markeredgecolor': '#4c9cff',  # 深粉红
        'markersize': 7,
        'color': '#4c9cff',            # 深粉红
        'linestyle': '-',
        'linewidth': 4,
    },
    {
        'marker': 's',
        'markerfacecolor': '#e7daf7',  # 浅蓝
        'markeredgecolor': '#af73fa',  # 深蓝
        'markersize': 6,
        'color': '#af73fa',            # 深蓝
        'linestyle': '-',
        'linewidth': 4,
    },
    {
        'marker': 'D',
        'markerfacecolor': '#ffd399',  # 浅紫
        'markeredgecolor': '#ffbb00',  # 深紫
        'markersize': 6,
        'color': '#ffbb00',            # 深紫
        'linestyle': '-',
        'linewidth': 4,
    },
    {
        'marker': 'p',
        'markerfacecolor': '#a1f2e9',  # 浅棕
        'markeredgecolor': '#59c4b8',  # 深棕
        'markersize': 6,
        'color': '#59c4b8',            # 深棕
        'linestyle': '-',
        'linewidth': 4,
    }
]


def read_csv_file(file_path):
    """
    读取 CSV 文件并返回 DataFrame。
    :param file_path: CSV 文件路径
    :return: Pandas DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        print("CSV 文件读取成功!")
        return df
    except Exception as e:
        print(f"读取 CSV 文件失败: {e}")
        return None

def compute_row_means(df, exclude_columns=None):
    """
    计算每一行的均值，排除指定列。
    :param df: Pandas DataFrame
    :param exclude_columns: 需要排除的列列表
    :return: 包含行均值的 Series
    """
    if "model" in df.columns:
        df = df.drop(columns=["model"], errors='ignore')
    if exclude_columns:
        df_numeric = df.drop(columns=exclude_columns, errors='ignore')
    else:
        df_numeric = df
    return df_numeric.mean(axis=1)


def plot_results(file_path):

    df = read_csv_file(file_path)
    
    total_tokens = df['model'].iloc[-1]

    x_axis = [float(ckpt_name.split("B")[0]) for ckpt_name in df['model'].tolist()]

    if "B" in total_tokens:
        total_tokens = float(total_tokens.replace("B", ""))

    if "model" in df.columns:
        df = df.drop(columns=["model"], errors='ignore')

    # 计算每一行的均值，排除指定列
    df['ave_wo_math_sat_cot'] = compute_row_means(df, exclude_columns=['math_sat-cot'])
    df['ave_wo_ocw_cot'] = compute_row_means(df, exclude_columns=['ocw-courses-cot'])
    df['average'] = compute_row_means(df, exclude_columns=None)

    all_columns = df.columns.tolist()

    print(f"all_columns: {all_columns}")

    # exit()
    plot_rows = len(all_columns) // 5 if len(all_columns) % 5 == 0 else len(all_columns) // 5 + 1

    import matplotlib.pyplot as plt
    # for each benchmark, plot 10 sub-figures to be 2x5, and make it high resolution
    plt.figure(figsize=(25, 5 * plot_rows))
    plt.rcParams['font.size'] = 20
    for i in range(0, len(all_columns)):
        print(f"plot {i} of {len(all_columns)}")
        plt.subplot(plot_rows, 5, i + 1 )
        # styles: grey dashline grid, white bg, black text
        plt.grid(linestyle='--')
        plt.xlabel('Training Tokens(B)')
        # plt.plot(range(0, len(df.iloc[:, i])), df.iloc[:, i], **style_hub[1])
        plt.plot(x_axis, df.iloc[:, i], **style_hub[1])
        plt.ylabel('Performance')
        # legend 扁一些
        # plt.legend(loc='lower right', fontsize='small')
        # benchmark name bold
        # plt.title(f'{benchmark_official_name_dict[df.columns[i]]}', fontweight='bold')
        plt.title(f'{df.columns[i]}')
    # big title
    plt.suptitle(f'Performance ({total_tokens}B)', fontweight='bold', fontsize=30)
    plt.tight_layout(pad=0.5)
    plt.show()
    plt.savefig(file_path.replace('.csv', '_plot.pdf'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dirname", type=str, default="outputs")
    parser.add_argument("--eval-atp", action='store_true')
    parser.add_argument("--isa-path", type=str, default="")
    parser.add_argument("--theory-file", type=str, default="")
    parser.add_argument("--summarize_dir", type=str, default="")
    args = parser.parse_args()

    model2dataset2task2metric = {}
    for model in os.listdir(args.dirname):
        model2dataset2task2metric[model] = {}
        subdir = os.path.join(args.dirname, model)
        for dataset in os.listdir(subdir):
            log_dir = os.path.join(subdir, dataset, "infer_logs")
            agg_dirname = os.path.join(subdir, dataset, "results")
            if not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)
                os.system(f"mv {subdir}/{dataset}/* {log_dir}")
            metric_paths = list(seek_metrics(log_dir))
            pred_paths = list(seek_predictions(log_dir))
            task2metric_paths = {'cot': [], 'tool': []}
            task2pred_paths = {'cot': [], 'tool': []}
            for path in metric_paths:
                if 'cot' in path:
                    task2metric_paths['cot'].append(path)
                else:
                    task2metric_paths['tool'].append(path)
            for path in pred_paths:
                if 'cot' in path:
                    task2pred_paths['cot'].append(path)
                else:
                    task2pred_paths['tool'].append(path)
            task2metric = {task: aggregate_metrics(paths) for task, paths in task2metric_paths.items()}
            task2pred = {task: aggregate_predictions(paths) for task, paths in task2pred_paths.items()}
            model2dataset2task2metric[model][dataset] = task2metric

            for task in task2metric:
                task_dirname = os.path.join(agg_dirname, task)
                os.makedirs(task_dirname, exist_ok=True)
                metric_path = os.path.join(task_dirname, "metrics.json")
                pred_path = os.path.join(task_dirname, "predictions.json")
                json.dump(task2metric[task], open(metric_path, "w"), indent=4)
                json.dump(task2pred[task], open(pred_path, "w"), indent=4)
                if 'minif2f' in dataset.lower() and 'isabelle' in dataset.lower() and task2pred[task] and args.eval_atp:
                    eval_path = metric_path + ".eval"
                    if os.path.exists(eval_path) and json.load(open(eval_path, "r")).get('n_samples', 0):
                        model2dataset2task2metric[model][dataset][task] = json.load(open(eval_path, "r"))
                        continue
                    print(f"Running minif2f-isabelle evaluation on {dataset} ...", flush=True)
                    print(f"Predictions >>> {pred_path}", flush=True)
                    cmd = f"PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python python unsafe_score_minif2f_isabelle.py " \
                        f"--isa-path {args.isa_path} " \
                        f"--theory-file {args.theory_file} " \
                        f"--working-dir {args.working_dir} " \
                        f"--port 9000 " \
                        f"--output {pred_path} "
                    os.system(cmd)

        if not os.path.exists(args.summarize_dir) or not os.path.exists(os.path.join(args.summarize_dir, model)):
            os.makedirs(args.summarize_dir, exist_ok=True)
            os.makedirs(os.path.join(args.summarize_dir, model), exist_ok=True)
        json.dump(
            model2dataset2task2metric[model], 
            open(os.path.join(args.summarize_dir, model, "evaluation_results.json"), "w"), 
            indent=4, 
            ensure_ascii=False
        )
    # aggregate results into one csv, column: dataset, row: model, value: accuracy
    # need to sort to avoid some cases brought by str not the number. 
    model2dataset2task2metric = dict(sorted(model2dataset2task2metric.items(), key=lambda item: float(item[0].split("B")[0])))

    csv_path = os.path.join(args.summarize_dir, "evaluation_results.csv")
    with open(csv_path, "w") as f:
        header = ['model']
        for dataset in model2dataset2task2metric[model]:
            for task in model2dataset2task2metric[model][dataset]:
                if 'accuracy' not in model2dataset2task2metric[model][dataset][task]:
                    continue
                header.append(f"{dataset}")
        f.write(",".join(header) + "\n")
        for model in model2dataset2task2metric:
            row = [model]
            for dataset in model2dataset2task2metric[model]:
                for task in model2dataset2task2metric[model][dataset]:
                    if 'accuracy' not in model2dataset2task2metric[model][dataset][task]:
                        continue
                    print(model, dataset, task, flush=True)
                    row.append(str(round(model2dataset2task2metric[model][dataset][task]['accuracy'] * 100, 4)))
            f.write(",".join(row) + "\n")
    
    if os.path.exists(csv_path):
        plot_results(csv_path)

if __name__ == '__main__':
    main()