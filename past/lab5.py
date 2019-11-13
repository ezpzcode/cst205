from PIL import Image
r = open('pixel.txt','r')
mystring = r.readlines()


emptylist = [] 
for x in mystring:
	y = x.rstrip(';\n')
	emptylist.append(y)

single = []
for x in emptylist:
	y = x.split()
	single.append(y)

#print(type(single[0][0]))

final = []
for x in single:
	for y in range(len(x)):
		final.append(int(x[y]))

mona = Image.frombytes('L',(18,29),bytes(final))

mona.show()