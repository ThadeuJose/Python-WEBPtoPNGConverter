from  main import  cli
import main
from click.testing import CliRunner

def create_runner(mocker, parameter_list):
    runner = CliRunner()
    mocker.patch("main.convert_webp_to_png")
    return runner.invoke(cli, parameter_list)

def test_cli_without_outputfolder(mocker):
    result = create_runner(mocker, ["-i","input_test"])
    dont_raise_exception(result)

def test_cli_folder_found(mocker):
    result = create_runner(mocker, ["-i","input_test","-o","output_test"])
    dont_raise_exception(result)

def test_cli_inputfolder_not_found(mocker):
    result = create_runner(mocker, ["-o","output_test"])
    raise_exception(result)

def test_cli_no_parameter(mocker):
    result = create_runner(mocker, [])
    raise_exception(result)

def test_cli_inputfile(mocker):
    inputpath = "input_test\\testimage.webp"
    outputpath = "input_test\\testimage.png"
    
    create_runner(mocker, ["-i", inputpath])
    
    main.convert_webp_to_png.assert_called_once_with(inputpath, outputpath, "png")

def test_cli_outputfolder_should_be_folder(mocker):
    result = create_runner(mocker, ["-i","input_test","-o","output_test\\testimage.png"])
    raise_exception(result)

def test_cli_inputfile(mocker):
    inputpath = "input_test\\testimage.webp"
    outputpath = "output_test\\testimage.png"
    
    create_runner(mocker, ["-i", inputpath, "-o","output_test"])
    
    main.convert_webp_to_png.assert_called_once_with(inputpath, outputpath, "png")

def raise_exception(result):
    assert result.exit_code > 0 

def dont_raise_exception(result):
    assert result.exit_code == 0