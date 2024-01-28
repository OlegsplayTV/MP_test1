import csv
import random


def task_4():
    f = open('resources/students_to_load.csv', encoding='utf-8')
    reader = list(csv.reader(f))
    countA = int(reader[-1][0])

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

    big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    pwd = [[]]
    for pwds in range(countA):
        doppwd = []
        pwd.append(doppwd)

    reader[0].append('login')
    reader[0].append('password')

    def f(x):
        forlog = reader[x][1].split(' ')
        Passwd = 0
        check = 0
        while check == 0:
            Passwd = random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(
                alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(
                alphabet)

            check = 0
            for i1 in small:
                for i2 in big:
                    for i3 in numbers:
                        if (i2 in Passwd) and (i2 in Passwd) and (i3 in Passwd):
                            check += 1

        login = f'{forlog[0]}_{forlog[1][0]}{forlog[2][0]}'
        pwd[x - 1].append(reader[x][1])
        pwd[x - 1].append(Passwd)
        reader[x].append(login)
        reader[x].append(Passwd)
        reader[x][-3] = reader[x][-3][:-4]

    for x in range(1, countA + 2):
        f(x)

    print(reader)
