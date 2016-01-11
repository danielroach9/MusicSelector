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