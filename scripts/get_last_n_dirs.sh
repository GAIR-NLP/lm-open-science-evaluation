#!/bin/bash

# 默认获取最后3层目录
LAYERS=3

# 检查是否提供了参数
if [ $# -eq 0 ]; then
    echo "Usage: $0 <path> [number_of_layers]"
    exit 1
fi

# 获取输入路径
PATH_INPUT="$1"

# 如果提供了第二个参数，使用它作为层数
if [ $# -eq 2 ] && [[ "$2" =~ ^[0-9]+$ ]]; then
    LAYERS=$2
fi

# 使用 awk 来获取最后N层目录
result=$(echo "$PATH_INPUT" | awk -F'/' '{
    path = "";
    for (i = NF - '"$LAYERS"' + 1; i <= NF; i++) {
        if (i > NF - '"$LAYERS"' + 1) path = path "/";
        path = path $i;
    }
    print path;
}')

# 输出结果
echo "$result"