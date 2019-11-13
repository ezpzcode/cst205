pixel_1 = (50, 1, 255)
pixel_2 = (23, 255, 20)
pixel_3 = (200, 255, 255)

pixel_list = [ pixel_1, pixel_2, pixel_3 ]

r_list = []
g_list = []
b_list = []

def approach_one(p_list):
    for pixel in p_list:
        r_list.append(pixel[0])
        g_list.append(pixel[1])
        b_list.append(pixel[2])
    r_list.sort()
    g_list.sort()
    b_list.sort()
    return (r_list[1], g_list[1], b_list[1])

print(approach_one(pixel_list))