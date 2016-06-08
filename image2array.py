from PIL import Image

im = Image.open("player.png")

pixels = im.load()


nbPixels = im.width * im.height
arrayStr = "static const bool array_name[{}] = {}\n".format(nbPixels, '{')
for y in range(0, im.width):
	arrayStr += "\t"
	for x in range(0, im.height):
		if pixels[x, y][0] == 0:
			arrayStr += "1, "
		else:
			arrayStr += "0, "
	arrayStr += "\n"

arrayStr += "};"


file = open("player.c", 'w')
file.write(arrayStr)
file.close()