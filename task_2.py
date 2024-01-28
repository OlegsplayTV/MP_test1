import csv

f = open('resources/students_to_load.csv', encoding='utf-8')
reader = list(csv.reader(f))
countA = int(reader[-1][0])


def task_2():
    z = 0
    for x in range(1, countA + 2):
        if '10' in reader[x][3]:
            z += 1
            names = reader[x][1].split(' ')
            print(f'{z} место: {names[1][:1]}. {names[0]}')
        if z == 3:
            break
