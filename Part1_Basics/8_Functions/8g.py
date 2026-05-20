# Make a dictionary describing a music album.
# Let the number of songs be a default paramter, set to None.

def make_album(artist, album_name, number_songs=None):
  if number_songs:
    album = {'artist': artist, 
           'album name': album_name, 
           'songs': number_songs}
  else:
    album = {'artist': artist, 
           'album name': album_name}
  return album

print(make_album('Kendrick Lamar', 'GNX'))
print(make_album('Fort Minor', 'The Rising Tied'))
print(make_album('Imagine Dragons', 'Night Visions', number_songs=12))

