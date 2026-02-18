#!/usr/bin/env python3
"""
语音转MD技能 - 语音转文字工具
支持音频和视频文件，自动检测并处理

使用方法:
    python3 voice_to_md.py <文件路径> [-o <输出文件>] [-k <API密钥>]

触发关键词:
    语音转文字, 语音转md, 音频转文字, 音频转md, 视频转文字, 视频转md, 转录
"""

import os
import sys
import argparse
import subprocess
import requests
from pathlib import Path
from typing import Optional


# ============== 配置 ==============
DEFAULT_API_URL = "https://api.siliconflow.cn/v1/audio/transcriptions"
DEFAULT_MODEL = "FunAudioLLM/SenseVoiceSmall"

AUDIO_EXTENSIONS = {'.mp3', '.wav', '.m4a', '.flac', '.ogg', '.aac', '.wma'}
VIDEO_EXTENSIONS = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'}


# ============== 核心函数 ==============
def get_api_key(api_key: Optional[str] = None) -> str:
    """获取 API 密钥"""
    if api_key:
        return api_key
    env_key = os.environ.get("SILICONFLOW_API_KEY")
    if env_key:
        return env_key
    raise ValueError("请提供 API 密钥：使用 -k 参数或设置 SILICONFLOW_API_KEY 环境变量")


def check_file_type(file_path: str) -> str:
    """判断文件类型"""
    ext = Path(file_path).suffix.lower()
    if ext in AUDIO_EXTENSIONS:
        return "audio"
    elif ext in VIDEO_EXTENSIONS:
        return "video"
    else:
        raise ValueError(f"不支持的文件格式: {ext}")


def extract_audio_from_video(video_path: str, output_path: str) -> str:
    """使用 ffmpeg 从视频提取音频"""
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"视频文件不存在: {video_path}")
    
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-vn",  # 不处理视频
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "16000",
        output_path
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"音频提取失败: {result.stderr}")
    
    if not os.path.exists(output_path):
        raise RuntimeError("音频提取后文件未生成")
    
    return output_path


def transcribe_audio(
    audio_path: str,
    api_key: str,
    model: str = DEFAULT_MODEL,
    api_url: str = DEFAULT_API_URL
) -> str:
    """调用 SiliconFlow API 转录音频"""
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"音频文件不存在: {audio_path}")
    
    file_size = os.path.getsize(audio_path)
    if file_size > 50 * 1024 * 1024:
        raise ValueError("文件大小超过 50MB 限制")
    
    headers = {"Authorization": f"Bearer {api_key}"}
    
    with open(audio_path, "rb") as audio_file:
        files = {
            "file": (os.path.basename(audio_path), audio_file),
            "model": (None, model)
        }
        
        response = requests.post(
            api_url,
            headers=headers,
            files=files,
            timeout=3600
        )
    
    response.raise_for_status()
    return response.json()["text"]


def voice_to_md(
    input_path: str,
    output_path: Optional[str] = None,
    api_key: Optional[str] = None,
    model: str = DEFAULT_MODEL,
    api_url: str = DEFAULT_API_URL
) -> str:
    """
    主函数：语音/视频转 Markdown
    
    Args:
        input_path: 输入文件路径
        output_path: 输出文件路径 (可选)
        api_key: SiliconFlow API 密钥
        model: 使用的模型
        api_url: API 端点
    
    Returns:
        转录的文本内容
    """
    # 获取 API 密钥
    api_key = get_api_key(api_key)
    
    # 检查文件类型
    file_type = check_file_type(input_path)
    
    # 处理视频：提取音频
    temp_audio = None
    try:
        if file_type == "video":
            print(f"检测到视频文件，正在提取音频...")
            temp_audio = input_path + ".temp_audio.mp3"
            extract_audio_from_video(input_path, temp_audio)
            audio_path = temp_audio
        else:
            audio_path = input_path
        
        # 转录音频
        print(f"正在转录音频...")
        text = transcribe_audio(audio_path, api_key, model, api_url)
        
        # 保存结果
        if output_path is None:
            output_path = str(Path(input_path).with_suffix(".md"))
        
        Path(output_path).write_text(text, encoding="utf-8")
        print(f"✅ 转录完成！结果已保存到: {output_path}")
        
        return text
        
    finally:
        # 清理临时文件
        if temp_audio and os.path.exists(temp_audio):
            os.remove(temp_audio)
            print(f"已清理临时文件: {temp_audio}")


# ============== 命令行入口 ==============
def main():
    parser = argparse.ArgumentParser(
        description="语音转MD工具 - 将音频/视频转为 Markdown 格式",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python3 voice_to_md.py audio.mp3
  python3 voice_to_md.py video.mp4 -o transcript.md
  python3 voice_to_md.py audio.wav -k YOUR_API_KEY
        """
    )
    
    parser.add_argument("input", help="输入的音频或视频文件路径")
    parser.add_argument("-o", "--output", help="输出的 Markdown 文件路径")
    parser.add_argument("-k", "--api-key", help="SiliconFlow API 密钥")
    parser.add_argument("-m", "--model", default=DEFAULT_MODEL,
                       choices=["FunAudioLLM/SenseVoiceSmall", "TeleAI/TeleSpeechASR"],
                       help="使用的模型")
    parser.add_argument("--url", default=DEFAULT_API_URL,
                       help="API 端点")
    
    args = parser.parse_args()
    
    try:
        voice_to_md(
            args.input,
            args.output,
            args.api_key,
            args.model,
            args.url
        )
    except Exception as e:
        print(f"❌ 错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
