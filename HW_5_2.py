#########################
#Author: Kuleshova Yana
#Date: 23/11/2021
#Task: 5_2
#########################

def febo(n):
    n = int(input("Введите конечное количество последовательностей: "))
    if n < 1:
        return None
    if n < 3:
        return 1

    fib_1 = fib_2 = 1
    fibi = 0
    for i in range(3, n + 1):
        fibi = fibi_1 + fibi_2
        fibi_1, fibi_2 = fibi_1, fibi
    return fibi