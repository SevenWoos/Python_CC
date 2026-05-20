# Make a dictionary describing a music album.
# Let the number of songs be a default paramter, set to None.

# Create a while loop to ask for albums. Include a quit value.

def make_album(artist, album_name, number_songs=None):
  if number_songs:
    album = {'artist': artist, 
           'album name': album_name, 
           'songs': number_songs}
  else:
    album = {'artist': artist, 
           'album name': album_name}
  return album

# print(make_album('Kendrick Lamar', 'GNX'))
# print(make_album('Fort Minor', 'The Rising Tied'))
# print(make_album('Imagine Dragons', 'Night Visions', number_songs=12))

while True:
  print("\nLet's create some albums!")
  
  artist = input("\nWhat is the artist's name? ")
  if artist == 'q':
    break

  album_name = input("\nWhat is the album name? ")
  if album_name == 'q':
    break

  number_songs = input("\nHow many songs are in the album? ")
  if number_songs == 'q':
    break
  
  album = {'artist': artist, 
           'album name': album_name, 
           'songs': number_songs}
  print(f"\n {album}")