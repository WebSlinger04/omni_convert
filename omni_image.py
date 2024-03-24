from PIL import Image, ImageSequence
import sys

def get_info():
    with open("data.txt", "r") as data:
        print(f"\n{data.read()}")


def write_info(line, user_input):
    with open("data.txt", "r") as data:
        data_read = data.readlines()
        data_read[line] = user_input + "\n"
    with open("data.txt", "w") as data:
        data.writelines(data_read)


def save_image(file_name):
    vid_sequence = []
    with Image.open(file_name) as image, open("data.txt","r") as data:
        name = input("\nWhat to name the file\n:")
        file = data.readlines()
        width,height = file[1].strip("\n").split(",")

        for frame in ImageSequence.Iterator(image):
            new_image = frame.resize([int(width),int(height)])
            new_image = new_image.convert(file[3].strip("\n").upper(),palette=Image.Palette.ADAPTIVE)
            vid_sequence.append(new_image)
        if file[2].strip("\n").lower() == "jpg":
            new_image.save(name + ".jpg","JPEG")
        elif len(vid_sequence) > 1:
            new_image.save(name +"." + file[2].strip("\n").lower(), file[2].strip("\n").upper(), save_all=True, append_images=vid_sequence)
        else:
            new_image.save(name +"." + file[2].strip("\n").lower(), file[2].strip("\n").upper(), append_images=vid_sequence)
    sys.exit()