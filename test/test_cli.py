from main import cli
from click.testing import CliRunner

def create_runner(parameter_list):
    runner = CliRunner()
    return runner.invoke(cli, parameter_list)

def test_cli_without_outputfolder():
    result = create_runner(["-i","input_test"])
    dont_raise_exception(result)

def test_cli_folder_found():
    result = create_runner(["-i","input_test","-o","output_test"])
    dont_raise_exception(result)

def test_cli_inputfolder_not_found():
    result = create_runner(["-o","output_test"])
    raise_exception(result)

def test_cli_no_parameter():
    result = create_runner([])
    raise_exception(result)

def raise_exception(result):
    assert result.exit_code == 1

def dont_raise_exception(result):
    assert result.exit_code == 0