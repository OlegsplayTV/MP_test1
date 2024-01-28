import csv
import operator


def task_1():
    # Открытие файла и добавление начальных переменных
    f = open('resources/students_to_load.csv', encoding='utf-8')
    CountOfScore = 0
    fsr2 = 0

    # Создание списка из каждой строки файла 'csv'
    reader = list(csv.reader(f))

    a = int(reader[-1][0])

    for x in range(1, a + 2):
        if reader[x][-1] != 'None':
            CountOfScore += 1
            fsr2 += int(reader[x][-1])
            reader[x][-1] = reader[x][-1] + '.000'

    sr = round(fsr2 / CountOfScore, 3)

    for x in range(1, a + 2):
        if reader[x][-1] == 'None':
            reader[x][-1] = str(sr)

    reader = sorted(reader, key=operator.itemgetter(4), reverse=True)

    name = str(input('Введите имя и фамилию через пробел: \n')).split(' ')
    for x in range(1, a + 2):
        if name[0] in reader[x][1]:
            if name[1] in reader[x][1]:
                print(f'Ты получил: {reader[x][-1][:-4]}, за проект - {reader[x][-3]}')
