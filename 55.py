import csv

p = 65
m = 10 ** 9 + 9
spis = "+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890:-'. "
f = open('game.txt', 'r', encoding='UTF-8')
reader = csv.DictReader(f, delimiter='$')
file = open('game_with_hash.csv', 'w', encoding='UTF-8')
writer = csv.writer(file)
writer.writerow(['hash', 'GameName', 'characters', 'nameError', 'date'])
for line in reader:
    hash = 0
    pstep = 0
    name = list(line['GameName'] + line['characters'])
    print(name)
    print(line)
    for i in range(0,len(name)):
        hash += spis.index(name[i]) * p ** pstep
        pstep += 1
    hash = hash % m
    writer.writerow([str(hash), line['GameName'], line['characters'], line['nameError'], line['date']])
