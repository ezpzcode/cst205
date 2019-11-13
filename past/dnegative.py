from PIL import Image
im = Image.open('negative.jpg')
def dnegative_image(pixel):
	return tuple(map(lambda a : 255 - a, pixel))
dnegative_list = map( dnegative_image, im.getdata() )

im.putdata(list(dnegative_list))
im.save('dnegative.jpg')
