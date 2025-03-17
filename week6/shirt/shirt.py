import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check()
    try:
        file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")

    shirt = Image.open("shirt.png")

    size = shirt.size
    muppet = ImageOps.fit(file, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])



def check():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if not check_extension(file1[1]) or not check_extension(file2[1]):
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extetions")



def check_extension(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False

if __name__ =="__main__":
    main()
