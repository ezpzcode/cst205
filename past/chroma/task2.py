from PIL import Image
im = Image.new("RGB", (700, 700), (255,255,255))
im.save("image.png", "PNG")

im1 = Image.open('image.png')
im2 = Image.open('otter.jpeg')
im3 = Image.open('cat.jpeg')
im4 = Image.open('giraffe.jpeg')

back_im = im1.copy()
back_im.paste(im2, (450, 400))
back_im.paste(im3, (100, 400))
back_im.paste(im4, (270, 150))
back_im.save('task2.jpeg', quality=95)