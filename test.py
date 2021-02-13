import os
from main import convert_webp_to_png, get_all_files, create_outputpath

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
    all_files = get_all_files('input_test')
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