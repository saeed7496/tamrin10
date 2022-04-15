
import pytube
class media:
    def __init__(self, p, n, d, i, url, du, c):
        self.product=p
        self.name=n
        self.director=d
        self.IMDBscore=i
        self.url=url
        self.duration=du
        self.casts=c
    def showinfo(self):
        print('prodoct type:',self.product,'\tname:',self.name,'\tdirector:',self.director,'\nIMDBscore:',self.IMDBscore,'\turladdres:',self.url,'\tduration:',self.duration,'\tcats:',self.casts)

    
    def edit_all(self):
        while True:
            i=int(input('pleaz choice for edit:\n1_type\t2_name\t3_director\n4_IMDB\tURL\t5_URL\t6_duration\t7_casts\t  8_exit\n: '))
            if i==1:
                self.product=input('new type: ')
            elif i==2:
                self.name=input('new name: ')
            elif i==3:
                self.director=input('new director name: ')
            elif i==4:
                self.IMDBscore=input('new IMDB: ')
            elif i==5:
                self.url=input('new URL: ')
            elif i==6:
                self.duration=input('new duration: ')
            elif i==7:
                self.casts=input('new casts(cast1-cast2-...: )')
            elif i==8:
                break
    

    def download(self):
        link =self.url
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename='test.mp4')

