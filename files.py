from os import listdir
from os.path import isfile, join
from pathlib import Path

EXTENSION = "png"
INPUT_EXTENSION = "webp"
OUTPUT_EXTENSION = "png"

def get_all_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def create_path(folder, filename, extension):
    return join(folder, filename + "." + extension)

def get_filename(filename):
    return Path(filename).stem

def get_path(filename):
    return Path(filename).parent.as_posix()