from files import get_all_files, get_filename, get_path, create_path

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

def test_create_path():
    folder = "output_test"
    filename = "testimage"
    extension = "png"    
    outputpath = "output_test\\testimage.png"
    response = create_path(folder, filename, extension)
    assert outputpath == response

def test_get_filename():
    assert get_filename("filename1.ext") == "filename1"

def test_get_filename_from_full_path():
    assert get_filename("mylibrary\\filename1.ext1.ext2") == "filename1.ext1"

def test_get_filename_multiples_ext():
    assert get_filename("filename1.ext1.ext2") == "filename1.ext1"

def test_get_path():
    assert get_path("E:\\Imagens\\Avatar\\5.png") == "E:/Imagens/Avatar"