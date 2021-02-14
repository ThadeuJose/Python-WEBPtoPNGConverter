import os
from unittest.mock import call
import main
from main import convert_webp_to_png, get_all_files, create_outputpath, convert_folder_webp_to_png



def test_converter():
    inputpath = "input_test/testimage.webp"
    outputpath = "output_test/testimage.png"
    file_extension = "png"
    if os.path.exists(outputpath):
        os.remove(outputpath)
    convert_webp_to_png(inputpath, outputpath,file_extension)
    assert os.stat(outputpath).st_size > os.stat(inputpath).st_size

def test_get_all_files():
    files = ["testimage.webp","testimage2.webp",
             "testimage3.webp","testimage4.webp",
             "testimage5.webp","testimage6.webp",
             "testimage7.webp"
            ]
    all_files = get_all_files("input_test")
    for i in range(len(all_files)):
        if files[i] != all_files[i]:
            print(files[i])
            print(all_files[i])
            assert False
    assert True

def test_create_outputpath():
    folder = "output_test"
    filename = "testimage"
    extension = "png"    
    outputpath = "output_test\\testimage.png"
    response = create_outputpath(folder, filename, extension)
    assert outputpath == response

def test_convert_folder_webp_to_png(mocker):
    inputfolder = "input_test"
    outputfolder = "output_test"
    file = "testimage1.webp"
    inputpath = inputfolder + "\\testimage1.webp"
    outputpath = outputfolder + "\\testimage1.png" 
    extension = "png"

    mocker.patch("main.convert_webp_to_png")
    mocker.patch(
        "main.get_all_files",
        return_value = [file]
    )

    convert_folder_webp_to_png(inputfolder, outputfolder)

    main.convert_webp_to_png.assert_called_once_with(inputpath,outputpath, extension)

def test_convert_multiples_folder_webp_to_png(mocker):
    inputfolder = "input_test"
    outputfolder = "output_test"
    files = ["testimage1.webp", "testimage2.webp", "testimage3.webp"]    
    extension = "png"

    mocker.patch("main.convert_webp_to_png")
    mocker.patch(
        "main.get_all_files",
        return_value = files
    )

    convert_folder_webp_to_png(inputfolder, outputfolder)

    calls = [call(inputfolder + "\\testimage1.webp", outputfolder + "\\testimage1.png", extension), 
             call(inputfolder + "\\testimage2.webp", outputfolder + "\\testimage2.png", extension),
             call(inputfolder + "\\testimage3.webp", outputfolder + "\\testimage3.png", extension),]

    main.convert_webp_to_png.assert_has_calls(calls)
