import csv

f = open('C:/Users/olegs/Downloads/students (1).csv', encoding='utf-8')
reader = list(csv.reader(f))
countA = int(reader[-1][0])

def task_3():
    CountOfScore = 0
    fsr2 = 0

    for x in range(1, countA + 2):
        if reader[x][-1] != 'None':
            CountOfScore += 1
            fsr2 += int(reader[x][-1])
            reader[x][-1] = reader[x][-1] + '.000'

    sr = round(fsr2 / CountOfScore, 3)

    for x in range(1, countA + 2):
        if reader[x][-1] == 'None':
            reader[x][-1] = str(sr)

    project = ''
    while project != 'СТОП':
        project = input('Введите номер проекта:\n')
        pscore = ''
        if project == 'СТОП':
            break
        for x in range(1, countA + 2):
            if reader[x][2] == str(int(project)):
                names = reader[x][1].split(' ')
                pscore = f'Проект №{project} делал: {names[1][:1]}. {names[0]} он(а) получил(а) оценку' \
                         f' - {reader[x][-1][:-4]}'

        if pscore == '':
            print('Ничего не найдено')
        else:
            print(pscore)