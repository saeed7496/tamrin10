
from Film import film
from Serise import series
from documentry import documentary
from Actor import actor
from class_media import media
from Clip import clip

class Main:
    def __init__(self):
        self.list_data=[]
        self.casts=[]
        file=open('datafilm.txt', 'r')
        row=file.read().split('\n')
        file.close()
        for i in range(len(row)):
            stone=row[i].split(',')
            cast=stone[6].split('-')
            for j in range(len(cast)):
                act=cast[j].split(' ')
                self.casts.append(actor(stone[1],act[0],act[1]))
            if stone[0]=='film':
                self.list_data.append(film(stone[0],stone[1],stone[2],stone[3],stone[4],stone[5],stone[6],stone[7]))
            elif stone[0]=='serise':
                self.list_data.append(series(stone[0],stone[1],stone[2],stone[3],stone[4],stone[5],stone[6],stone[7]))
            elif stone[0]=='clip':
                self.list_data.append(clip(stone[0],stone[1],stone[2],stone[3],stone[4],stone[5],stone[6],stone[7]))
            elif stone[0]=='documentary':
                self.list_data.append(documentary(stone[0],stone[1],stone[2],stone[3],stone[4],stone[5],stone[6],stone[7]))
            
    def show_data(self):
        t=input('pleaz inter type (film or serise or clip or documentary): ')
        for data in self.list_data:
            if data.product==t:
                data.showinfo()
    
    def show_casts(self):
        t=input('pleaz inter name movie:')
        print('casts:')
        for act in self.casts:
            if act.name_movie==t:
                act.show_act()
        print()
            
    def show_menu(self):
        dict_menu={1:'Add', 2:'Edit ', 3:'Delet',
            4:'search', 5:'show list', 6:'casts', 7:'search plus', 8:'download', 9:'save & exit'}

        for i,j in dict_menu.items():
            print(i,'=',j)

    def add(self):
        new_type=input('pleaz choise new type (film\tserise\tclip\tdocumentary) for add: ')
        if new_type=='film' or new_type=='serise' or new_type=='clip' or new_type=='documentary':
            new_t=input('pleaz inter type:')
            new_n=input('pleaz inter name:')
            new_d=input('pleaz inter director:')
            new_i=input('pleaz inter IMDB:')
            new_url=input('pleaz inter url:')
            new_du=input('pleaz inter duration:')
            new_c=input('pleaz inter casts(cast1-cast2,...):')
            if new_type=='film':
                new_g=input('pleaz inter genre:')
                self.list_data.append(film(new_t,new_n,new_d,new_i,new_url,new_du,new_c,new_g))
            elif new_type=='serise':
                new_count=input('pleaz inter count of series: ')    
                self.list_data.append(series(new_t,new_n,new_d,new_i,new_url,new_du,new_c,new_count))
            elif new_type=='clip':
                new_ma=input('pleaz inter nam of music artist: ')
                self.list_data.append(clip(new_t,new_n,new_d,new_i,new_url,new_du,new_c,new_ma))
            elif new_type=='documentary':
                new_o=input('pleaz inter object: ')
                self.list_data.append(documentary(new_t,new_n,new_d,new_i,new_url,new_du,new_c,new_o))
            print('added')
        else:
            print('type not found try again... ')
    
    def edit(self):
        print('pleaz inter type and name for edit: ')
        t=input('type: ')
        n=input('name: ')
       
        for j in self.list_data:
            if j.product==t=='film'and j.name==n:
                media.edit_all(j)       
                film.edit_spicial(j)
                print('edited')
                break
            elif j.product==t=='serise' and n==j.name:
                media.edit_all(j)
                series.edit_spicial(j)
                print('edited')
                break
            elif j.product==t=='clip' and n== j.name:
                media.edit_all(j)
                clip.edit_spicial(j)
                print('edited')
                break
            elif j.product==t=='documentary' and n==j.name:
                media.edit_all(j)
                documentary.edit_spicial(j)
                print('edited')
                break
            elif j==self.list_data[-1] :
                print('not found!')
                break

    def download(self):
        print('pleaz inter type and name for download: ')
        t=input('type: ')
        n=input('name: ')
        for data in self.list_data:
            if data.product==t and data.name==n:
                data.download()
            elif data==self.list_data[-1]:
                print('not found!')

    def delete(self):
        print('pleaz inter type and name for delet: ')
        t=input('type: ')
        n=input('name: ')
        for data in self.list_data:
            if data.product==t and data.name==n:
                self.list_data.remove(data)

    def search(self):
        print('pleaz inter type and name for search: ')
        t=input('type: ')
        n=input('name: ')
        for data in self.list_data:
            if data.product==t and data.name==n:
                data.showinfo()
                break
            elif data==self.list_data:
                print('not found')        

    def search_plus(self):
        t1=float(input('pleaz inter a first time: '))
        t2=float(input('pleaz inter second time: '))
        for data in self.list_data:
            if t1 <= float(data.duration) < t2:
                data.showinfo()
                o=open('tamrin10.txt' , 'w').close
                b=open('tamrin10.txt','a')
                t=str(data)
                b.write(t)
                b.write('\n')
    
    def save(self):
        o=open('datafilm.txt' , 'w').close
        b=open('datafilm.txt','a')
        for data in self.list_data:
            st=str(data.product)+','+str(data.name)+','+str(data.director)+','+str(data.IMDBscore)+','+str(data.url)+','+str(data.duration)+','+str(data.casts)
            b.write(st)
            b.write(',')
            if data.product=='film':
                b.write(data.genre)
            elif data.product=='serise':
                b.write(data.count)
            elif data.product=='clip':
                b.write(data.music_artist)
            elif data.product=='documentary':
                b.write(data.object)
            if data==self.list_data[-1]:
                break
            b.write('\n')
s=Main()           
while True:
    print('well come...')
    s.show_menu()
    y=int(input('pleaz chooze a number: '))
    if y == 1:
        s.add()
    elif y==2:
        s.edit()
    elif y== 3:
        s.delete()
        print('deleted')
    elif y == 4:
        s.search()
    elif y== 5:
        s.show_data()
    elif y==6:
        s.show_casts()
    elif y==7:
        s.search_plus()
    elif y==8:
        s.download()
    elif y==9:
        s.save()
        break
    