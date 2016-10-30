import os
import string
import random
import sys

alphabet = list(string.ascii_lowercase)

def main():
	for i in range(100):
		artist = createName(8)
		for j in range(100):
			song = createName(10)
			filename = artist + " - " + song + ".mp3"
			f = open("/home/peter/Music/Disc1/" + filename, 'w+')
			f.close()

def createName(length):
	res = ""
	for i in range(length):
		res += alphabet[random.randrange(0, len(alphabet))]
	return res

main()

