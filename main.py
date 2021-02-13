from PIL import Image

def convert_webp_to_png(inputpath, outputpath, file_extension):
    im = Image.open(inputpath).convert("RGB")
    im.save(outputpath, file_extension)

inputpath = "input/1 - The Flight.webp"
outputpath = "output/1 - The Flight.png"
file_extension = "png"
convert_webp_to_png(inputpath, outputpath,file_extension)
