from os import sep
import random
boarda=[]
h=0
j=0
while h<9:
        boarda.append([])
        while j<9:            
                boarda[h].append("-")
                j+=1
        j=0
        h+=1



boardm=[]
k=-3
l=0
m=1
while m<10:
        if m%3-1==0:
                l=0
                k+=3
        
        boardm.append([[k,l],[k,l+1],[k,l+2],[k+1,l],[k+1,l+1],[k+1,l+2],[k+2,l],[k+2,l+1],[k+2,l+2]])
        l+=3
        m+=1



sayilar=(1,2,3,4,5,6,7,8,9)


def yazdir():
        a=0
        b=0
        while a<9:
                print(boarda[a][b]+"  "+boarda[a][b+1]+"  "+boarda[a][b+2]+"    "+boarda[a][b+3]+"  "+boarda[a][b+4]+"  "+boarda[a][b+5]+"    "+boarda[a][b+6]+"  "+boarda[a][b+7]+"  "+boarda[a][b+8]+"    ")
                
                if a==2 or a==5:
                        print("")
                a+=1
        
                

g=0                                             #9 boardın herbirinin bir elemanın rastgele rndm listesinden verdirme
rndm=[1,2,3,4,5,6,7,8,9]
while g<9:   
        v,v2=random.choice(boardm[g]) #boardm[0][5] 
        q=random.choice(rndm)
        rndm.remove(q)
        boarda[v][v2]=str(q)
        g+=1

boardz=boarda
#boardz=[]
#for i in boarda:
#        boardz.append(i)


      
print(boardz)

yazdir()

while True:
        
        while True:
                
                dongukontrol=True
                basasar=False
                sayi=input("Bir sayi seçiniz. (*tahtayi resetlemek 'r',cikmak icin 'q' giriniz.)" )
                
                
                if sayi=="r":
                        print("if calisyr")
                        boarda=boardz
                        print(boarda)
                        
                        break
                elif sayi=="q":
                        quit()
                konum_satir,konum_sutun=input("bir konum seçiniz.*format: (konum satir,konum sütun)").split(",")

                sayi=int(sayi)
                konum_satir=int(konum_satir)
                konum_sutun=int(konum_sutun)
                
                if sayi and konum_satir and konum_sutun in sayilar:
                        pass

        
                t=0
                while t<9:
                        if str(sayi) == boarda[konum_satir-1][t]:
                                yazdir()
                                print("Bu satirin "+str(t+1)+". karesinde zaten "+str(sayi)+" sayisi var")
                                dongukontrol=False
                                t=9
                                break
                        if str(sayi) == boarda[t][konum_sutun-1]:  
                                yazdir()
                                print("Bu sutunun "+str(t+1)+". karesinde zaten "+str(sayi)+" sayisi var")
                                dongukontrol=False
                                
                                break  
                        t+=1
                n=0
                hangikare=""
                while n<9:
                        for a,b in boardm[n]:
                                if a==konum_satir-1 and b==konum_sutun-1:
                                        hangikare=n
                                        n=9
                                        break
                        n+=1
                konum=konum_satir-1,konum_sutun-1
                p=0
                while p<9:
                        for a,b in boardm[hangikare]:

                                if str(sayi)==str(boarda[a][b]):
                                        yazdir()
                                        print("3x3'lük alanda zaten sayi bulunuyor") 
                                        dongukontrol=False
                                        p=9
                                        break
                                        
                                
                        p+=1
                
               
                if dongukontrol==True and boarda[konum_satir-1][konum_sutun-1]=="-":
                #sayi in boarda[0:9][konum_satir-1]:      
                        boarda[konum_satir-1][konum_sutun-1]=str(sayi)
                        yazdir()
                

                                

                                
                        