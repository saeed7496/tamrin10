from class_media import media

class series(media):
    def __init__(self, p, n, d, i, url,du, c, count):
        media.__init__(self,p, n, d, i, url, du, c)
        self.count=count
    def showinfo(self):
        media.showinfo(self)
        print('number count: ',self.count)

    def edit_spicial(self):
        qu=int(input('change count?\n1_yes\t2_no:'))
        if qu==1:
            self.count=input('count: ')