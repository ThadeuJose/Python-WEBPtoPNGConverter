from PIL import Image
from os import listdir
from os.path import isfile, join

def convert_webp_to_png(inputpath, outputpath, file_extension):
    im = Image.open(inputpath).convert("RGB")
    im.save(outputpath, file_extension)

def get_all_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def create_outputpath(folder, filename, extension):
    return join(folder, filename+"."+extension)

inputpath = "input/1 - The Flight.webp"
outputpath = "output/1 - The Flight.png"
file_extension = "png"
convert_webp_to_png(inputpath, outputpath,file_extension)
