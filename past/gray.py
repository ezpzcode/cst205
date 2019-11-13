from PIL import Image
im = Image.open('mona.jpg')
def lum_image(p):
 new_red = int(p[0] * 0.299)
 new_green = int(p[1] * 0.587)
 new_blue = int(p[2] * 0.114)
 luminance = new_red + new_green + new_blue
 return (luminance,) * 3
new_list = map( lum_image, im.getdata() )
im.putdata(list(new_list))
im.save('negative.jpg')