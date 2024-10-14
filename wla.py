inp = input()

ls = inp.split("\n")
n = inp[0]

stats = {}
pojedynki = []

for i in range(int(n)):
    s, z = inp[i + 1].split(" ")
    stats[i] = [int(s), int(z)] # siła , zręcznośc, 

# for i in range(int(n)):
#     si = stats[i][0]
#     zi = stats[i][1]
#     for j in range(int(n)):
#         if i == j:
#             continue
#         else:
#             sj = stats[j][0]
#             zj = stats[j][1]
#             if si > sj or zi > zj:
#                 stats[i][2].append(j)
#             elif sj > si or zj > zi:
#                 stats[j][2].append(i)

for i in range(n):
    si = stats[i][0]
    zi = stats[i][1]
    for j in range(int(n)):
        if i == j:
            continue
        else:
            sj = stats[j][0]
            zj = stats[j][1]
            if si > sj or zi > zj:
                stats[i][2].append(j)
            elif sj > si or zj > zi:
                stats[j][2].append(i)
