task_file=eval/lighteval_recommended_set.txt
default_output_dir=outputs_lighteval

lighteval accelerate "pretrained=${1}" ${2:-${task_file}} --dataset-loading-processes 66 --output-dir="${3:-${default_output_dir}}"  --max-samples 1000 --override-batch-size 4


# /mbz/users/fan.zhou/backup/storage/ckpts/OLMo-2-0325-32B-stage1-step721000-tokens6049B
