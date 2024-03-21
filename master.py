from PIL import Image
import sys
import os

import omni_image

def file_exists(file_name):
    if not os.path.isfile(file_name):
        print("File paramater or file doesnt exist")
        sys.exit()


def check_extension(file_name):
    valid_image_extensions = (".png",".jpg",".jpeg",".tiff",".bmp",".webp",".mp4",".pdf",".gif")
    valid_video_extensoins = (".mp4",".pdf",".gif")
    if file_name.endswith(valid_image_extensions or valid_video_extensoins):
        print(f"{file_name} accessed")
    else:
        print(f"{file_name} contains a invalid file extension")
        print(f"{valid_image_extensions}\n{valid_video_extensoins}")
        sys.exit()


def write_inital_data(file_name):
    file_size = round(os.path.getsize(file_name) / 1024 ** 2,1)
    with Image.open(file_name) as image:
        original_data = [f"{image.filename}\n",
                         f"{image.size}\n".replace(" ","").replace("(","").replace(")",""),
                         f"{image.format}\n",f"{image.mode}\n",
                         f"{file_size}MB"]
    with open("data.txt", "w") as data:
        data.writelines(original_data)


def program_options():
    user_input = input("\nDo you want to info, resize, convert, save, or quit?\n:")
    match user_input.lower():
        case "info":
            omni_image.get_info()
        case "resize":
            omni_image.resize_image()
        case "convert":
            omni_image.convert_image()
        case "save":
            omni_image.save_image(sys.argv[1])
        case "quit":
            sys.exit()
        case _:
            print("input not understood")
    program_options()

def main():
    file_exists(sys.argv[1])
    check_extension(sys.argv[1])
    write_inital_data(sys.argv[1])
    program_options()

main()