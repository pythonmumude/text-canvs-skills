---
name: 语音转MD技能
description: 将音频或视频转为 Markdown 格式的转录文本。支持自动检测文件类型，视频自动提取音频后转录。
trigger_keywords:
  - 语音转文字
  - 语音转md
  - 音频转文字
  - 音频转md
  - 视频转文字
  - 视频转md
  - 转录
  - transcribe
  - 语音转markdown
---

# 语音转MD技能

将音频或视频转为 Markdown 格式的转录文本。

## 触发方式

当用户说以下关键词时自动调用：
- 语音转文字 / 语音转md / 语音转markdown
- 音频转文字 / 音频转md
- 视频转文字 / 视频转md
- 转录 / transcribe

## 使用方法

### 前置准备

```bash
# 安装 ffmpeg (视频提取音频需要)
brew install ffmpeg

# 安装依赖
pip3 install --break-system-packages requests

# 设置 API 密钥
export SILICONFLOW_API_KEY="sk-eornvjxjcpelpmgnrizcupotgzlojnikuaqxojmgnzcwqqms"
```

### 命令行使用

```bash
# 基本用法 - 音频
python3 /Users/mumu/Downloads/opencode/豆包/voice_to_md.py audio.mp3

# 指定输出文件
python3 /Users/mumu/Downloads/opencode/豆包/voice_to_md.py audio.mp3 -o transcript.md

# 视频文件（自动提取音频）
python3 /Users/mumu/Downloads/opencode/豆包/voice_to_md.py video.mp4 -o result.md

# 指定 API 密钥
python3 /Users/mumu/Downloads/opencode/豆包/voice_to_md.py audio.mp3 -k YOUR_API_KEY

# 选择模型
python3 /Users/mumu/Downloads/opencode/豆包/voice_to_md.py audio.mp3 --model TeleAI/TeleSpeechASR
```

## 支持格式

### 音频格式
- MP3, WAV, M4A, FLAC, OGG, AAC, WMA

### 视频格式
- MP4, AVI, MOV, MKV, FLV, WMV

## 限制

- 单个文件最大 50MB
- 音频最长 1 小时
- 视频会自动提取音频后再转录

## 内部流程

```
1. 检查文件是否存在
2. 判断文件类型（音频/视频）
3. 如果是视频 → 使用 ffmpeg 提取音频，当音频文件超过一小时，把它处理为两段分别调用转录，转好后合并
4. 调用 SiliconFlow API 转录
5. 保存为 .md 文件
6. 清理临时文件
```

## API 配置

- **提供商**: SiliconFlow
- **模型**: FunAudioLLM/SenseVoiceSmall (默认), TeleAI/TeleSpeechASR
- **端点**: https://api.siliconflow.cn/v1/audio/transcriptions
- **环境变量**:   sk-eornvjxjcpelpmgnrizcupotgzlojnikuaqxojmgnzcwqqms

## 示例场景

```bash
# 1. 播客转文字
python3 voice_to_md.py podcast.mp3 -o podcast.md

# 2. 会议录音转文字
python3 voice_to_md.py meeting.wav -o meeting.md

# 3. 视频字幕提取
python3 voice_to_md.py lecture.mp4 -o lecture.md

# 4. 批量转录 (需要自己写脚本循环调用)
for f in *.mp3; do
  python3 voice_to_md.py "$f" -o "${f%.mp3}.md"
done
```

## 错误处理

| 错误 | 解决方法 |
|------|----------|
| No module named 'requests' | `pip3 install --break-system-packages requests` |
| ffmpeg not found | `brew install ffmpeg` |
| API 密钥错误 | 检查 SILICONFLOW_API_KEY 环境变量 |
| 文件过大 | 分割文件到 50MB 以下 |
| 请求超时 | 音频过长，耐心等待（最长1小时） |
