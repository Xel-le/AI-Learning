import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith((".png", ".jpg", ".jpeg")):
    sys.exit("Only .png, .jpg and .jpeg files are supported")

if sys.argv[1].endswith(".png") and not sys.argv[2].endswith(".png"):
    sys.exit("Specified files must have the same extensions")
elif sys.argv[1].endswith(".jpg") and not sys.argv[2].endswith(".jpg"):
    sys.exit("Specified files must have the same extensions")
elif sys.argv[1].endswith(".jpeg") and not sys.argv[2].endswith(".jpeg"):
    sys.exit("Specified files must have the same extensions")

with open("shirt.png", "rb") as shirt_file:
    shirt_image = Image.open(shirt_file)
    shirt_height = shirt_image.height
    shirt_width = shirt_image.width

    with open(sys.argv[1], "rb") as before_image_file:
        before_image = Image.open(before_image_file)
        before_image_fit = ImageOps.fit(before_image, (shirt_width, shirt_height))
        before_image_fit.paste(shirt_image, (0,0), shirt_image)
        before_image_fit.save(sys.argv[2])

