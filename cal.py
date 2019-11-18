from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s,str(x))
    #print(x)


hesap = 7
s1=0
def islemler(x):
    global hesap
    hesap = x
    global s1
    s1 = float(giris.get())
    print(hesap)
    print(s1)
    giris.delete(0,'end')

s2 = 0
def hesapla():
    global s2
    s2= float(giris.get())
    print(s2)
    global hesap
    sonuc = 0
    if (hesap == 0) :
        sonuc = s1 + s2
    elif (hesap == 1):
        sonuc= s1 - s2
    elif (hesap == 2):
        sonuc = s1 * s2
    elif (hesap == 3):
        sonuc = s1 / s2
    elif (hesap == 4):
        sonuc = s1 % s2
    elif (hesap == 5):
        sonuc = (sonuc) / s1
    elif (hesap == 6):
        sonuc = s1 * s1
    giris.delete(0,'end')
    giris.insert(0,str(sonuc))


pencere = Tk() #pencere boyutu
pencere.geometry("350x400")

giris = Entry(font= "Verdana 14 bold", width= 20, justify=RIGHT)
giris.place (x=20,y=20)


b = []
for i in range(1,10):
    b.append( Button(text = str(i), font = "Verdana 14 bold",width=3, command = lambda x=i:yaz(x)))

nb = Button(text = ".", fg = "GREEN", font = "Verdana 14 bold", width=3, command = lambda x='.':yaz(x))
nb.place(x=30, y=275)

sb = Button(text = "0", font = "Verdana 14 bold", width=3, command = lambda x=0:yaz(x))
sb.place(x=85, y=275)


sayac = 0
for i in range (0,3):
    for j in range (0,3):
        b[sayac].place(x=30+j*55,y=110+i*55)
        sayac+= 1

islem = []

for i in range(0,7):
    islem.append(Button(font="Verdana 14 bold", width=3, command=lambda x=i:islemler(x)))

islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"
islem[4]['text'] = "%"
islem[5]['text'] = "√"
islem[6]['text'] = "x²"

for i in range(0,4):
    islem[i].place(x=195,y=110+55*i)

mod = Button(text = "%",fg = "PURPLE", font = "Verdana 14 bold", width=3, command = lambda x="%":yaz(x))
mod.place(x=30, y=60)

kok = Button(text = "√", fg = "PINK", font = "Verdana 14 bold", width=3, command = hesapla)
kok.place(x=85, y=60)

kare = Button(text = "x²", fg = "BLUE", font = "Verdana 14 bold", width=3, command = hesapla)
kare.place(x=140, y=60)

clean = Button(text = "C", fg = "BLUE", font = "Verdana 14 bold", width=3, command = hesapla)
clean.place(x=195, y=60)

sil = Button(text = "<--", fg = "BLUE", font = "Verdana 14 bold", width=3, command = hesapla)
sil.place(x=250, y=60)


esit = Button(text = "=", fg = "RED", font = "Verdana 14 bold",width=3, command = hesapla)
esit.place(x=140, y=275)



pencere.mainloop()