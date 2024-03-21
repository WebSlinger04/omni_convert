from PIL import Image

def get_info():
    with open("data.txt", "r") as data:
        print(f"\n{data.readline()}{data.readline()}{data.readline()}{data.readline()}{data.readline()}")


def resize_image():
    size = input("\nWhat resolution to resize to? (ex:1920,1080)\n:")
    with open("data.txt", "r") as data:
        data_read = data.readlines()
        data_read[1] = size + "\n"
    with open("data.txt", "w") as data:
        data.writelines(data_read)

def convert_mode(type):
    is_alpha = ["png", "tiff","webp","gif"]
    with open("data.txt", "r") as data:
        data_read = data.readlines()
        if type == is_alpha:
            data_read[3] = "RGBA\n"
        else:
            data_read[3] = "RGB\n"
    with open("data.txt", "w") as data:
        data.writelines(data_read)

def convert_image():
    convert = input("\nWhat extension to convert to:\n").strip(".")
    with open("data.txt", "r") as data:
        data_read = data.readlines()
        data_read[2] = convert + "\n"
    with open("data.txt", "w") as data:
        data.writelines(data_read)
    convert_mode(convert)


def save_image(file_name):
    name = input("What to name the file:\n")
    with Image.open(file_name) as image, open("data.txt","r") as data:
        file = data.readlines()
        width,height = file[1].strip("\n").split(",")
        new_image = image.resize([int(width),int(height)])
        new_image = image.convert(file[3].strip("\n"))
        if file[2].strip("\n") != "jpg":
            new_image.save(name + "." + file[2].strip("\n"),file[2].strip("\n"))
        else:
            new_image.save(name + ".jpg","jpeg")