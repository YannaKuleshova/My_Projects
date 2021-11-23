#########################
#Author: Kuleshova Yana
#Date: 23/11/2021
#Task: 5_1
#########################

def factorial(n):
    n = int(input("Введите количество последовательностей: "))
    if n < 0:
        return None
    if n < 2:
        return 1

    factor_val = 1
    for i in range(2, n + 1):
        factor_val *= i
    return factor_val        
