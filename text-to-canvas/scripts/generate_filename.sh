#!/bin/bash
# 生成Canvas文件名
# 用法: ./generate_filename.sh "主题名称"

if [ $# -eq 0 ]; then
    echo "Usage: $0 \"主题名称\""
    exit 1
fi

THEME="$1"
DATE=$(date +%Y-%m-%d)
# 移除特殊字符，保留中文、英文、数字
CLEAN_THEME=$(echo "$THEME" | sed 's/[^[:alnum:]\u4e00-\u9fa5]/-/g' | sed 's/-\+/-/g' | sed 's/^-//;s/-$//')

FILENAME="${DATE}_${CLEAN_THEME}.canvas"
echo "$FILENAME"
