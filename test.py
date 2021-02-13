import os
from main import convert_webp_to_png

def test_converter():
    inputpath = "input_test/testimage.webp"
    outputpath = "output_test/testimage.png"
    file_extension = "png"
    if os.path.exists(outputpath):
        os.remove(outputpath)
    convert_webp_to_png(inputpath, outputpath,file_extension)
    assert os.stat(outputpath).st_size > os.stat(inputpath).st_size
