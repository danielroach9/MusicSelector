__author__ = 'dcr'


class MusicFile:
    artist = ''
    title = ''
    album = ''
    abspath = ''

    def __init__(self, artist, name, album, path):
        self.artist = artist
        self.title = name
        self.album = album
        self.abspath = path

    def __repr__(self):
        return "MusicFile(%s, %s, %s)" % (self.artist, self.title, self.abspath)

    def __eq__(self, other):
        if isinstance(other, MusicFile):
            return (self.artist == other.artist) and (self.title == other.title) and (self.abspath == other.abspath)
        else:
            return False

    def __hash__(self):
        return hash(self.__repr__())

    def __str__(self):
        return "Artist: " + self.artist + "\nTitle: " + self.title + \
               "\nAlbum: " + self.album + "\nLocation @: " + self.abspath + "\n"
    
    def getArtist(self):
        return self.artist

    def getTitle(self):
        return self.title

    def getAlbum(self):
        return self.album

    def getAbsPath(self):
        return self.abspath

