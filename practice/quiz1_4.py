my_info = 'The capital of France is Paris.'

top_weekend_movies = ['Black Panther', 'Peter Rabbit', 'Fifty Shades Freed', 'Jumanji: Welcome to the Jungle', 'The 15:17 to Paris']

movie_name = my_info[-6:-1] + ' Blues'

if movie_name in top_weekend_movies:
	print(f'{movie_name} made it into the top moves!')
else :
	print(f'Darn, {movie_name} didn\'t make it into the top movies.')
