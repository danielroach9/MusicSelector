__author__ = 'dcr'

from MusicFile import *
import eyed3
import os

collection = '/Users/dcr/Music/iTunes/iTunes Media/Music/'
featureArray = ["feat.", "featuring", "ft."]



def iterateThroughMusic():

    for subdir, dirs, files in os.walk(collection):
        for item in files:
            tp = os.path.splitext(item)
            if tp[1] != '.mp3':
                continue
            else:
                print
                song = eyed3.load(os.path.join(subdir, item))
                print song.tag.title
                print song.tag.artist


def printArtistOccurrence(name):

    # lowercase the given string to be case insensitive
    name = name.lower()

    # goes through all files and subdirectories in a specified directory
    for subdir, dirs, files in os.walk(collection):
        for item in files:

            # splits the name of the file and the file's extension into a tuple
            # checks if the file is an mp3 file or not
            tp = os.path.splitext(item)
            if tp[1] != '.mp3':
                continue
            else:

                # uses os.path.join to combine the file name and its path to get absolute path
                # loads the music file w/ eyed3 package
                data = eyed3.load(os.path.join(subdir, item))

                # if eyed3 can load the file (needs to be mp3), take the title and artist from ID3 tags
                if data is not None:
                    title = data.tag.title
                    artist = data.tag.artist

                    # if either one of these is none, do nothing
                    if artist is None or title is None:
                        continue

                    # if both are found, lowercase both strings so to be case insensitive
                    else:
                        artist = artist.lower()
                        title = title.lower()

                        # if the given search string is in the artist, this most likely means that
                        # this is the artist we are looking for, print out song info
                        if name in artist:
                            print
                            print data.tag.title
                            print data.tag.artist

                        # if the given search string is in the title, try to check and see if they
                        # are featured in the song (to avoid inaccurate queries as best as possible)
                        elif name in title:
                            if any(word in title for word in featureArray):
                                print
                                print data.tag.title
                                print data.tag.artist
                        else:
                            continue

def getSongs(songSet, querySet):

    for subdir, dirs, files in os.walk(collection):
        for item in files:

            # splits the name of the file and the file's extension into a tuple
            # checks if the file is an mp3 file or not
            tp = os.path.splitext(item)
            if tp[1] != '.mp3':
                continue
            else:

                # uses os.path.join to combine the file name and its path to get absolute path
                # loads the music file w/ eyed3 package
                data = eyed3.load(os.path.join(subdir, item))

                # if eyed3 can load the file (needs to be mp3), take the title and artist from ID3 tags
                if data is not None:
                    title = data.tag.title
                    artist = data.tag.artist

                    # if either one of these is none, do nothing
                    if artist is None or title is None:
                        continue

                    # if both are found, lowercase both strings so to be case insensitive
                    else:
                        artist = artist.lower()
                        title = title.lower()

                        for search in querySet:
                            if search.done() is not True:
                                if search.getArtist() in artist:
                                    songSet.add(MusicFile(search.getArtist(), data.tag.title, data.tag.album, os.path.join(subdir, item)))
                                    search.incrementFound()
                                elif search.getArtist() in title:
                                    if any(word in title for word in featureArray):
                                        songSet.add(MusicFile(search.getArtist(), data.tag.title, data.tag.album, os.path.join(subdir, item)))
                                        search.incrementFound()
                                else:
                                    continue

printArtistOccurrence("Chance")

