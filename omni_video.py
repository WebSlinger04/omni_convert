import moviepy.editor as moviepy
import sys
import glob
import os

def save_video(file_name):
    name = input("\nWhat to name the file\n:")
    include_audio = input("\nDo you want to include audio (True or False)\n:")
    with open("data.txt","r") as data:
        data_read = data.readlines()
        width,height = data_read[1].strip("\n").split(",")

        clip = moviepy.VideoFileClip(file_name, target_resolution=(int(height),int(width)), audio=include_audio)
        clip.write_videofile(name + "." + data_read[2].strip("\n").lower(), codec='libx264', audio_codec='pcm_s32le')
    sys.exit()

def create_timelapse_video(folder_path):

    img_seq = glob.glob(os.path.join(folder_path, '*'))
    img_seq.sort()
    name = input("\nWhat to name the file\n:")
    with open("data.txt","r") as data:
        data_read = data.readlines()

        try:
            clip = moviepy.ImageSequenceClip(img_seq, fps=int(data_read[4].strip("\n").lower()))
        except Exception:
            clip = moviepy.ImageSequenceClip(img_seq, fps=30)
        
        try:
            clip.write_videofile(f'{name}.{data_read[2].strip("\n").lower()}')
        except Exception:
            clip.write_videofile(f'{name}.mp4')
        clip.close
    sys.exit()