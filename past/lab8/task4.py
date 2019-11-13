class Song:
	def __init__(self, name, artist, genre, length, album):
		self.name = name
		self.artist = artist
		self.genre = genre
		self.length = length 
		self.album = album

mysong = Song("Imagine", "Avril Lavigne", "pop", "187sec", "Instant Karma")
print(mysong.name)
print(mysong.artist)
print(mysong.genre)
print(mysong.length)
print(mysong.album)