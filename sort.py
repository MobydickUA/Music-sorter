import os
import glob

path = os.path.join(os.getcwd(), "Disc1")
sortpath = os.path.join(os.getcwd(), "Disc2")
artists = []

for f in os.listdir(path):
	artists.append(f.split(" - ")[0])

artists = set(artists)
for artist in artists:
	artist = artist.lower().title()
	destPath = os.path.join(sortpath, artist)
	songs = glob.glob(path + os.sep + artist.lower() + "*")

	if os.path.isdir(destPath):
		for song in songs:
			songName = song.split(" - ")[1])
			os.rename(song, os.path.join(destPath, songName)
			print("Moved: " + artist + " - " + songName)
	else:
		if len(songs) >= 3:
			if not os.path.isdir(destPath):
				os.makedirs(destPath)
				print("Created folder: " + artist)
			for song in songs:
				songName = song.split(" - ")[1])
				os.rename(song, os.path.join(destPath, songName))
				print("-Moved: " + artist + " - " + songName)
