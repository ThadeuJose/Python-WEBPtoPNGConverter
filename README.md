# Python-WEBPtoPNGConverter
WEBP to PNG image converter write in Python

# Environment 

## Run Environment 
venv\Scripts\activate

## Quit Environment 
deactivate

## Run test 
python -m pytest test.py

## Create the requirements file
python -m pip freeze > requirements.txt

# TODO 
V1 

- ~~Convert all archives from folder input from webp to png~~ 

V2

- Use a command line 
    webpconverter -i input -o output
   
- Build with pyinstaller 


# Technical Debt 

- Wrong inputs
    - Test cli 
        - Check if is a ouput folder is a folder
            @click.option("-o","--output", type=click.Path(exists=True, file_okay=False), help="Path of the output folder")
        - If output folder was not given, the program should put the image in the same place else should put in the output folder     
				https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix
				https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem
        - https://click.palletsprojects.com/en/7.x/testing/
        - https://stackoverflow.com/questions/53203500/unittest-for-click-module         
- Show in the command line the current status
    - progress bar or echo 

# Sources

[Testing stdout](https://docs.pytest.org/en/stable/capture.html)

https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df

[Pyinstaller](http://www.pyinstaller.org/)

[Click file path arguments](https://click.palletsprojects.com/en/7.x/arguments/#file-path-arguments)

https://medium.com/@ajeet214/image-type-conversion-jpg-png-jpg-webp-png-webp-with-python-7d5df09394c9

https://changhsinlee.com/pytest-mock/