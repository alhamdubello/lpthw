#basic fo writing classes

#Declare class with attributes and methods

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#use classes created
# 
happy_bday = Song(["Happy Birthday to you",
                    "I don't want ot get sued",
                    "So i;will stip right there"])

bulls_on_a_parade = Song(["There is a rally around the family",
                           "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_a_parade.sing_me_a_song()

