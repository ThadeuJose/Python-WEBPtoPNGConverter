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

def convert_folder_webp_to_png(inputfolder, outputfolder):
    EXTENSION = "png"
    for file in get_all_files(inputfolder):        
        new_file = file.replace("webp", "png")
        convert_webp_to_png(join(inputfolder, file), join(outputfolder,new_file), EXTENSION)
    

inputpath = "input"
outputpath = "output"
file_extension = "png"

# convert_folder_webp_to_png(inputpath, outputpath)
