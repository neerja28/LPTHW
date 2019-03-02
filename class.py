class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print (line)

bday = Song(["Happy Birthday to you"])
anthem  = Song (["Jana gana mana"])

bday.sing()
anthem.sing()
