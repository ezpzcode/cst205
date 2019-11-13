import math
from PIL import Image

target_color = (19, 255, 9)
max_dist = 250


def color_distance(color_1, color_2):
    red_diff = math.pow((color_1[0] - color_2[0]), 2)
    green_diff = math.pow((color_1[1] - color_2[1]), 2)
    blue_diff = math.pow((color_1[2] - color_2[2]), 2)
    return math.sqrt(red_diff + green_diff + blue_diff)

def remove_chroma(a, b):
    dist = color_distance(target_color, b)
    if dist > max_dist:
        return(a)
    alpha = (dist / max_dist) ** 2
    new_pixel = (int(alpha * b[0] + (1 - alpha) * a[0]),
                 int(alpha * b[1] + (1 - alpha) * a[1]),
                 int(alpha * b[2] + (1 - alpha) * a[2]))
    return (new_pixel)

def chromakey(src, dest):
    offset_x = src.width - dest.width
    offset_y = src.height - dest.height
    dest_x = 0
    for src_x in range(offset_x, src.width):
            dest_y = 0
            for src_y in range(offset_y, src.height):
                src_pixel = src.getpixel((src_x, src_y))
                new_pixel = src_pixel
                if (dest_y < dest.height and dest_x < dest.width):
                    dest_pixel = dest.getpixel((dest_x,dest_y)) 
                    if color_distance(target_color, dest_pixel) > max_dist:
                        new_pixel = dest_pixel
                    else:
                        new_pixel = remove_chroma(src_pixel, dest_pixel)
                src.putpixel((src_x,src_y), new_pixel)
                dest_y += 1
            dest_x += 1
    return src

background = Image.open("jungle.jpg")
greenscreen = Image.open("zebra.jpg")

new_image = chromakey(background, greenscreen)
new_image.show()
new_image.save("task3.jpg")

