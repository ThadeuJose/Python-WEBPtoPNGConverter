from PIL import Image
from os import listdir
from os.path import isfile, join

def convert_webp_to_png(inputpath, outputpath, file_extension):
    MODE = "RGB"
    im = Image.open(inputpath).convert(MODE)
    im.save(outputpath, file_extension)

def get_all_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def create_path(folder, filename, extension):
    return join(folder, filename + "." + extension)

def get_filename(filename):
    return filename[0:filename.find(".")]

def convert_folder_webp_to_png(inputfolder, outputfolder):
    EXTENSION = "png"
    INPUT_EXTENSION = "webp"
    OUTPUT_EXTENSION = "png"
    for file in get_all_files(inputfolder):        
        filename = get_filename(file)
        convert_webp_to_png(create_path(inputfolder, filename, INPUT_EXTENSION), 
                            create_path(outputfolder,filename, OUTPUT_EXTENSION), 
                            EXTENSION)
    

inputpath = "input"
outputpath = "output"
file_extension = "png"

convert_folder_webp_to_png(inputpath, outputpath)
