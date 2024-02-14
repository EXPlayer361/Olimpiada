import csv

f = open('game.txt', 'r', encoding='UTF-8')
reader = csv.DictReader(f, delimiter='$')
file = open('game_new.txt', 'w', encoding='UTF-8')
writer = csv.writer(file)
writer.writerow(['GameName', 'characters', 'nameError', 'date'])
for line in reader:
    if line['nameError'].split(':')[1] == '55':
        cha = line['characters']
        er = line['nameError']
        gam = line['GameName']
        dat = line['date']
        print(f'У персонажа {cha} в игре {gam} нашлась ошибка с кодом: {er}. Дата фиксации: {dat}')
        line['nameError'] = 'Done'
        line['date'] = '0000-00-00'
    writer.writerow([line['GameName'], line['characters'], line['nameError'], line['date']])
