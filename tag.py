import os
import taglib

path = "/Users/blakenicholson/Music/iTunes/iTunes Media/Music/Compilations/BETAPACK vs TOTAL TRAX/01 Backfire.mp3"
song = taglib.File(path)
print(song.tags)