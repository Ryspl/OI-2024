#SKOŃCZONE ZADANIE
# TEORETYCZNIE USPRAWNIC


a, b = input().split(" ")

a = int(a)
b = int(b)

modA = a%2
modB = b%2

wynik = 0

# if a == b:
#       wynik = 2

if modA == modB:
        wynik =  b - a

else: #elif (modA == 1 and modB == 0) or (modA == 0 and modB == 1):
    if ((b - a + 1) / 2) % 2 == 0:
        wynik = b - a + 1
    else:
        wynik = b - a - 1

print(wynik)
