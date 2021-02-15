import os
from unittest.mock import call
import converters
from converters import convert_folder_webp_to_png, convert_webp_to_png

def test_converter():
    inputpath = "input_test/testimage.webp"
    outputpath = "output_test/testimage.png"
    file_extension = "png"
    if os.path.exists(outputpath):
        os.remove(outputpath)
    convert_webp_to_png(inputpath, outputpath,file_extension)
    assert os.stat(outputpath).st_size > os.stat(inputpath).st_size


def test_convert_folder_webp_to_png(mocker):
    inputfolder = "input_test"
    outputfolder = "output_test"
    file = "testimage1.webp"
    inputpath = inputfolder + "\\testimage1.webp"
    outputpath = outputfolder + "\\testimage1.png" 
    extension = "png"

    mocker.patch("converters.convert_webp_to_png")
    mocker.patch(
        "converters.get_all_files",
        return_value = [file]
    )

    convert_folder_webp_to_png(inputfolder, outputfolder)

    converters.convert_webp_to_png.assert_called_once_with(inputpath,outputpath, extension)

def test_convert_multiples_folder_webp_to_png(mocker):
    inputfolder = "input_test"
    outputfolder = "output_test"
    files = ["testimage1.webp", "testimage2.webp", "testimage3.webp"]    
    extension = "png"

    mocker.patch("converters.convert_webp_to_png")
    mocker.patch(
        "converters.get_all_files",
        return_value = files
    )

    convert_folder_webp_to_png(inputfolder, outputfolder)

    calls = [call(inputfolder + "\\testimage1.webp", outputfolder + "\\testimage1.png", extension), 
             call(inputfolder + "\\testimage2.webp", outputfolder + "\\testimage2.png", extension),
             call(inputfolder + "\\testimage3.webp", outputfolder + "\\testimage3.png", extension),]

    converters.convert_webp_to_png.assert_has_calls(calls)

