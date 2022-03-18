# from pakiet import *
#
# napis = 'dziś jest piątek'
# litery.wyswietl(napis)
# print(litery.dlugosc(napis))
# print(dodawanie.dzielenie(5,5))

# plik=open('lab4text.txt','r')
# znak=plik.read(10)
# linia=plik.readline()
# wiersze=plik.readline()


# plik.close()
# print(znaki)
# print(linia)
# print(wiersze)

# import sys
# print('Podaj kierunek studiów, rok i specjalizację')
# dane=sys.stdin.readline()

# plik=open('dane.txt','w+')
# plik.write(dane)
# plik.close()
# lista=[]
# for i in range(0,11):
#     lista.append(i)
# plik=open('dane.txt','a+')
# plik.writelines(str(lista))
# plik.close()

# with open('lab4text.txt','r') as plik:
#     for linia in plik:
#         print(linia,end='')

# class PierwszaKlasa:
#     """Pierwsza klasa python"""
#     atrybut=54321
#     def pierwsza_metoda(self):
#         return 'pierwsza metoda klasy'

# obiekt=PierwszaKlasa()
# print(obiekt)
# print(obiekt.atrybut)
# obiekt.tekst='napis'
# print(obiekt.tekst)
# # obiekt2=PierwszaKlasa()
# # print(obiekt2.tekst)
# print(obiekt.pierwsza_metoda())

class Ksztalty:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.opis='To będzie klasa dla ogólnych kształtów'

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2*self.x + 2*self.y

    def dodaj_opis(self,text):
        self.opis = text

    def skalowanie(self,czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik

prostokat=Ksztalty(10,30)
print(prostokat.pole())
print(prostokat.obwod())
print(prostokat.opis)
prostokat.dodaj_opis('prostokąt')
prostokat.skalowanie(0.5)
print(prostokat.x)
print(prostokat.y)