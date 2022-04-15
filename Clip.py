from class_media import media

class clip(media):
    def __init__(self, p, n, d, i, url, du, c, ma):
        media.__init__(self, p, n, d, i, url, du, c)
        self.music_artist=ma

    def showinfo(self):
        media.showinfo(self)
        print('music artist is:',self.music_artist)

    def edit_spicial(self):
        qu=int(input('change muic artist?\n1_yes\t2_no:'))
        if qu==1:
            self.music_artist=input('music artist: ')


