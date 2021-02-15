import click 

@click.command()
@click.option("-f","--filename", type=click.Path(exists=True), help="Input file")
@click.option("-i","--inputfolder", type=click.Path(exists=True), help="Path of the input folder")
@click.option("-o","--outputfolder", type=click.Path(exists=True), help="Path of the output folder")
def cli(filename, inputfolder, outputfolder):
    """
    Program that convert images from webp to png 
    """
    print(filename)
    print(inputfolder)
    print(outputfolder)

if __name__ == "__main__":
    cli()