from PIL import Image

im = Image.open('emil.jpg')

im_flipped = im.transpose(method=Image.TRANSPOSE)

im_flipped.save('transpose.jpg')