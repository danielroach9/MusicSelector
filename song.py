__author__ = 'dcr'


class Song:
    artist = ''
    title = ''
    abspath = ''

    def __init__(self, artist, name, path):
        self.artist = artist
        self.title = name
        self.abspath = path

    def __repr__(self):
        return "Song(%s, %s, %s)" % (self.artist, self.title, self.abspath)

    def __eq__(self, other):
        if isinstance(other, Song):
            return ((self.artist == other.artist) and (self.title == other.title) and (self.abspath == other.abspath))
        else:
            return False

    def __hash__(self):
        return hash(self.__repr__())

    
    def getArtist(self):
        return self.artist

    def getTitle(self):
        return self.title

    def getAbsPath(self):
        return self.abspath

