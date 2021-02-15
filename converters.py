from PIL import Image

from files import EXTENSION, INPUT_EXTENSION, OUTPUT_EXTENSION, create_path, get_all_files, get_filename


def convert_webp_to_png(inputpath, outputpath, file_extension):
    MODE = "RGB"
    im = Image.open(inputpath).convert(MODE)
    im.save(outputpath, file_extension)

def convert_folder_webp_to_png(inputfolder, outputfolder):    
    for file in get_all_files(inputfolder):        
        filename = get_filename(file)
        convert_webp_to_png(create_path(inputfolder, filename, INPUT_EXTENSION), 
                            create_path(outputfolder,filename, OUTPUT_EXTENSION), 
                            EXTENSION)
