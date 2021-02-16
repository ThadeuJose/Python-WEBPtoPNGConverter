from converters import convert_webp_to_png
import click 
from files import OUTPUT_EXTENSION, EXTENSION, create_path, get_filename, get_path 
from converters import convert_webp_to_png

@click.command()
@click.option("-i","--input", required=True, type=click.Path(exists=True), help="Path of the input folder or file")
@click.option("-o","--output", type=click.Path(exists=True, file_okay=False), help="Path of the output folder")
def cli(input, output):
    """
    Program that convert images from webp to png 
    """
    if not output:        
        output = get_path(input) 
    
    convert_webp_to_png(input, create_path(output,get_filename(input), OUTPUT_EXTENSION), EXTENSION)
    

if __name__ == "__main__":
    cli()