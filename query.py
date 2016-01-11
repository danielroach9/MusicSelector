__author__ = 'dcr'


class Query:
    artist = ''
    desiredNum = 0
    found = 0

    def __init__(self, artist, amount):
        self.artist = artist
        self.artist.lower()
        self.amount = amount
        self.found = 0

    def __repr__(self):
        return "Query(%s, %s, %s)" % (self.artist, self.amount, self.found)

    def __eq__(self, other):
        if isinstance(other, Query):
            return self.artist == other.artist
        else:
            return False

    def __hash__(self):
        return hash(self.__repr__())

    def __str__(self):
        return "Looking for songs w/ " + self.artist + "\n" + self.found + "/" + self.desiredNum + " found\n"
    
    def getArtist(self):
        return self.artist

    def getAmount(self):
        return self.desiredNum

    def getFound(self):
        return self.found

    def incrementFound(self):
        self.found += 1

    def done(self):
        return self.found == self.desiredNum