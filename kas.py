#from kaslib import DajN, Pytaj, Szturchnij, Odpowiedz
from random import *

#Pytaj(y) - poda nwd x i y
#Szturchnij() - zmaian x na inny
#Odpowiedz(y) - sprawdza x=y i zwiększa wygrane o jeden

def Pytaj(y, x):
    while y != x:
        if y > x:
            y -= x
        else:
            x -= y

    return y

def Szturchnij():
    return randint(1, n)

def Odpowiedz(y):
    print("TAK") if y == x else print("NIE")



liczba_bajtalarów = 10 ** 7
n = 10 ** 18 #DajN()

szukana = Szturchnij()
dzielniki = list()

while liczba_bajtalarów > 0:
    #pytając o NWD znajdź liczbę
    pass
