last_n_dirs=${2:-3}
echo model_base_dir: $model_base_dir
echo last_n_dirs: $last_n_dirs

model_dirs=()
for dir in "$model_base_dir"/*/; do
    if [ -d "$dir" ]; then
        model_dirs+=("$dir")
        echo "Found model directory: $dir"
    fi
done
echo model_dirs: ${model_dirs[@]}

if [ ${#model_dirs[@]} -eq 0 ]; then
    echo "Error: No model directories found in $model_base_dir"
    exit 1
fi
echo "Found ${#model_dirs[@]} model directories to evaluate"