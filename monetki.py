# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.

# Входные данные
# В первой строке входного файла INPUT.TXT записано натуральное число N (1 ≤ N ≤ 100) – число монеток. 
# В каждой из последующих N строк содержится одно целое число – 1 если монетка лежит решкой вверх 
# и 0 если вверх гербом.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите минимальное количество монет, которые нужно перевернуть.

def main():
    input_file = open('C:\PYTHON\monetki\input.txt', 'r')
    output_file = open('output.txt', 'w')
    line = input_file.readline().split()
    n = int(line[0])
    k = 0
    m = 0
    for i in range(n):
        line = input_file.readline().split()
        if int(line[0]) == 0:
            k = k + 1
        if int(line[0]) == 1:
            m = m + 1
    print(m, k)
 
    if m > k:
        ans = k
    else:
        ans = m
 
 
    print(ans)
    output_file.write(str(ans) + "\n")
 
 
if __name__ == "__main__":
    main()