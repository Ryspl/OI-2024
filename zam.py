# SKOŃCZONE ZADANIE ZAMEK CYKLICZNY
# MOŻLIWE USPRAWNIENIE PRZYGOTOWANIA
import time
import random
#SPRAWDZIC DLACZEGO JEST 0 PUNKTÓW

# x = 9 * 10 ** 999999

def test():
    # return "".join([f'{random.randint(0, 9)}' for x in range(10000000)])
    # return f'9' + '0' * 999999
    return input()




def przycisk1(n):
    addon = 9 - int(n[-1])
    # n[:-1] + '9'
    # p1 = n[1:]
    # p2 = n[0]
    # n = p1 + p2
    # n = n.removeprefix('0')

    return n[:-1] + '9', addon 

def przycisk2(n):
    # func_start = time.perf_counter()
    p1 = n[1:]
    p2 = n[0]
    c = p1 + p2
    c = c.removeprefix('0')
    # func_end = time.perf_counter()
    # print(f"przycisk 2 time: {func_end - func_start}s")
    return c

stepCount = 0



def przygotowanie(n = str()):
    global stepCount
    func_start = time.perf_counter()
    table = {48 : None}
    if n[-1] != '0':
        n = n.translate(table)  
    else:
        n = n.translate(table) + '0'
    n = n.rstrip('9') if n[-1] != '9' else n.rstrip('9') + '9'
    func_end = time.perf_counter()
    print(f"przygotowanie time: {func_end - func_start}s")
    return n




p_start = time.perf_counter()

n = test() # 9 * 10 ** 999999

p_end = time.perf_counter()
print(f'calculaton of the initial str() time: {p_end - p_start}s')


n = przygotowanie(n)

n2 = n




func_start = time.perf_counter()

steps = 0

if n2 == '10' or n2 == '1':
    steps = 1 
else:    
    for ch in n2:
        # if ch == '0':
            # continue
        steps += 10 - int(ch) if ch != '0' else 1
    steps += 1

func_end = time.perf_counter()

print(f'{steps} \t {func_end - func_start}s')







start = time.perf_counter()


while n != '1':
    if len(n) == n.count('9'):
        stepCount += 2
        break

    elif n[-1] == '0':
        # func_start = time.perf_counter()
        n = przycisk2(n)
        # func_end = time.perf_counter()
        # print(f'przycisk 2 time: {func_end - func_start}s')
        stepCount += 1
    
    elif n[-1] != '9':
        # func_start = time.perf_counter()
        n, addon = przycisk1(n)
        n = przycisk2(n)
        # func_end = time.perf_counter()
        # print(f'przycisk 1 + 2 time: {func_end - func_start}s')
        stepCount += addon + 1

    else:
        # func_start = time.perf_counter()
        n = przycisk2(n)
        # func_end = time.perf_counter()
        # print(f'przycisk 2 time: {func_end - func_start}s')
        stepCount += 1
end = time.perf_counter()
print(f"main loop time : {end - start}s")
# ileStep(n)




print(f'\n{stepCount}')
