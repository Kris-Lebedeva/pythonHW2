# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

'''n = int(input('Введите количество монет: '))
heads = 0
tails = 0

for i in range(n):
    x = int(input())
    if x == 0:
        heads += 1
    else:
        tails += 1
if tails > heads:
    print(heads)
else:
    print(tails)'''

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

'''s = int(input('cумма двух чисел: \n'))
p = int(input('произведение чисел: \n'))
for i in range(s):
    for j in range(p):
        if s == i + j and p == i * j:
            print(i, j)'''

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

'''n = int(input("Введите число N: "))
i = 0
while 2 ** i <= n:
    print(2 ** i, end=' ')
    i += 1 '''


