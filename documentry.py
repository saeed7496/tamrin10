from class_media import media

class documentary(media):
    def __init__(self, p, n, d, i, url, du, c, o):
        media.__init__(self,p, n, d, i, url, du, c)
        self.object=o

    def showinfo(self):
        media.showinfo(self)
        print('object:',self.object)

    def edit_spicial(self):
        qu=int(input('change object?\n1_yes\t2_no:'))
        if qu==1:
            self.object=input('object: ')

