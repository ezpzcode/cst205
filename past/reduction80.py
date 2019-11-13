from PIL import Image
im = Image.open('mona.jpg')
def map_BlueandGreen(pixel):
	return (int(pixel[0]), int(pixel[1]*.2), int(pixel[2]*.2))
new_list = map(map_BlueandGreen, im.getdata())
im.putdata(list(new_list))
im.save('reduction80.jpg')
