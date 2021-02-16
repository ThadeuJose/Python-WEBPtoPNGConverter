import click 
from click import ClickException

@click.command()
@click.option("-i","--input", type=click.Path(exists=True), help="Path of the input folder or file")
@click.option("-o","--output", type=click.Path(exists=True), help="Path of the output folder")
def cli(input, output):
    """
    Program that convert images from webp to png 
    """
    print(input)
    print(output)
    if not input:
        raise ClickException("Should give a input folder or file")
    

if __name__ == "__main__":
    cli()