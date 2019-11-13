list = [1, 2]
tuple = (1, 2)
dict = {'1':1, '2':2}

def is_in(val, type):
	if val in type:
		print('true')
	else:
		print('false')

is_in(1, list)
is_in(1, tuple)
is_in('1', dict)
is_in(2, dict)
