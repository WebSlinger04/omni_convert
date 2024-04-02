from PIL import Image
from pillow_heif import register_heif_opener
import sys
import cv2
import os

import omni_image
import omni_video

def file_exists(file_name):
    if not(os.path.isfile(file_name) or os.path.isdir(file_name)):
        print("File paramater or file doesnt exist")
        sys.exit()
    if os.path.isdir(file_name):
        return "Sequence"
    return "File"


def check_extension(file_name):
    valid_extensions = (".png",".jpg",".jpeg",".bmp",".webp","heic",".gif",".tiff",".mp4",".avi", ".mov", "mkv") #could include exr and raw
    if file_name.endswith(valid_extensions):
        print(f"{os.path.basename(file_name)} accessed")
    else:
        print(f"{os.path.basename(file_name)} contains a invalid file extension")
        print(f"{valid_extensions}")
        sys.exit()

def write_inital_data(file_name):
    file_size = round(os.path.getsize(file_name) / 1024 ** 2,1)
    try:
        with Image.open(file_name) as image:
            original_data = [f"{os.path.basename(file_name)}\n",
                            f"{image.width},{image.height}\n",
                            f"{str(os.path.splitext(file_name)).strip(")'").split(".")[1]}\n",
                            f"{image.mode}\n",
                            f"{file_size}MB"]
    except:
        file = cv2.VideoCapture(file_name)
        original_data = [f"{os.path.basename(file_name)}\n",
                f"{int(file.get(cv2.CAP_PROP_FRAME_WIDTH))},{int(file.get(cv2.CAP_PROP_FRAME_HEIGHT))}\n",
                f"{str(os.path.splitext(file_name)).strip(")'").split(".")[1]}\n",
                f"Cant Identify Color Mode\n",
                f"{file_size}MB"]
    with open("data.txt", "w+") as data:
        data.writelines(original_data)


def program_options(file_type):
    if file_type == "File":
        user_input = input("\nDo you want to info, resize, convert, mode, save, or quit?\n:")
    else:
        user_input = input("\nDo you want to convert, fps, save, or quit?\n:")
    match user_input.lower():
        case "info":
            omni_image.get_info()
        case "resize":
            omni_image.write_info(1, input("\nChange resolutions to (ex:1920,1080)\n:"))
        case "convert":
            omni_image.write_info(2, input("\nChange File extension to\n:"))
        case "mode":
            omni_image.write_info(3, input("\nChange color mode to\n:"))
        case "fps":
            omni_image.write_info(4, input("\nChange fps to\n:"))
        case "save":
            if file_type == "Sequence":
                omni_video.create_timelapse_video(sys.argv[1])
            try:
                omni_image.save_image(sys.argv[1])
            except Exception:
                omni_video.save_video(sys.argv[1])
        case "quit":
            sys.exit()
        case _:
            print("input not understood")
    program_options(file_type)

def main():
    register_heif_opener()
    file_type = file_exists(sys.argv[1])
    if file_type == "File":
        check_extension(sys.argv[1])
        write_inital_data(sys.argv[1])
    program_options(file_type)

main()