#_*_coding:utf-8_*_
#作者       ：  Deth
#创建时间    : 2020/5/13 14:52
#文件       ： 合并. py
# IDE       : PyCharm

import os
import shutil
import subprocess
from ffmpy import FFmpeg

path = os.path.join(os.getcwd(),'B站视频')

path_lists = os.listdir(path)

for name in path_lists:
    ts_path = os.path.join(path, name)
    print(ts_path)
    vediolist = os.listdir(ts_path)
    vedio_path = os.path.join(ts_path,'vedio.m4s')
    audio_path = os.path.join(ts_path,'audio.m4s')


    command = f"ffmpeg -i {vedio_path} -i {audio_path} -c copy {ts_path}.mp4"
    subprocess.call(command, shell=True)


    shutil.rmtree(ts_path)
