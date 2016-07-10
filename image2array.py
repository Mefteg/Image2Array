import argparse
import os

from PIL import Image

parser = argparse.ArgumentParser(
    description='Convert an image to an array (1 -> Black, 0 -> White).'
    )
parser.add_argument('image')

args = parser.parse_args()

imName = os.path.splitext(os.path.basename(args.image))[0]

im = Image.open(args.image)

pixels = im.load()

nbPixels = im.width * im.height
arrayStr = "#define {}_WIDTH {}\n".format(imName.upper(), im.width)
arrayStr += "#define {}_HEIGHT {}\n".format(imName.upper(), im.height)
arrayStr += "static const bool {}[{}] = {}\n".format(imName.upper(), nbPixels, '{')
for y in range(0, im.width):
	arrayStr += "\t"
	for x in range(0, im.height):
		if pixels[x, y][0] == 0:
			arrayStr += "1, "
		else:
			arrayStr += "0, "
	arrayStr += "\n"

arrayStr += "};"


file = open("{}.c".format(imName), 'w')
file.write(arrayStr)
file.close()