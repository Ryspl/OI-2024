# SKOŃCZONE ZADANIE ZAMEK CYKLICZNY
# MOŻLIWE USPRAWNIENIE PRZYGOTOWANIA
import time
#SPRAWDZIC DLACZEGO JEST 0 PUNKTÓW

a = time.perf_counter()

def przycisk1(n):
    return str(int(n) + 1)

def przycisk2(n):
    n = str(n)
    p1 = n[1:]
    p2 = n[0]
    c = p1 + p2
    x = True
    while x:
        if c.startswith('0'):
            c = c[1:]
        else:
            x = False
    return c

stepCount = 0

def przygotowanie(n = str()):
    global stepCount
    if n[-1] == '0':
        n = n.rstrip("0")
    stepCount += 1
    return n


n = 9 * 10 ** 999999


n = str(n)
# n = przygotowanie(n)


while n != '1':
    if len(n) == n.count('9'):
        n = przycisk1(n)
        n = przycisk2(n)
        stepCount += 2
        break
    elif n[-1] == '0':
        n = przycisk2(n)
        stepCount += 1
    
    elif n[-1] != '9':
        n = przycisk1(n)
        stepCount += 1

    else:
        n = przycisk2(n)
        stepCount += 1
   

print(stepCount)
b = time.perf_counter()
print(f'\n {b-a}s')
