color_counter = {}

def add_one(color):
	if color in color_counter:
		color_counter[color] += 1
	else:
		color_counter[color] = 1

add_one('shamrock')
add_one('cornflower blue')
add_one('granny sith apple')
add_one('shamrock')

print(len(color_counter))