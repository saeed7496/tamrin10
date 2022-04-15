from class_media import media

class film(media):
    def __init__(self, p, n, d, i, url, du, c, g):
        media.__init__(self, p, n, d, i, url, du, c)
        self.genre=g
    
    def showinfo(self):
        media.showinfo(self)
        print('genre:',self.genre)

    def edit_spicial(self):
        qu=int(input('change genre?\n1_yes\t2_no:'))
        if qu==1:
            self.genre=input('genre: ')



