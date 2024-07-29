import cv2
import subprocess
import numpy as np

def stream_video(input_file, output_url):
    # 打开视频文件
    cap = cv2.VideoCapture(input_file)
    
    # 获取视频属性
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # 设置FFmpeg命令
    command = [
        'ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', f'{width}x{height}',
        '-r', str(fps),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-f', 'mpegts',
        output_url
    ]
    
    # 启动FFmpeg进程
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # 将帧写入FFmpeg进程
        process.stdin.write(frame.tobytes())
    
    # 清理资源
    cap.release()
    process.stdin.close()
    process.wait()

# 使用示例
input_file = 'input.mp4'
output_url = 'udp://127.0.0.1:1234'
stream_video(input_file, output_url)