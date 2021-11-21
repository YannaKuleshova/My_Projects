#########################
#Author: Kuleshova Yana
#Date: 21/11/2021
#Task: 4_3
#########################

# Определение функции вычисления высокосного года
def is_year_leap (year):
    year = int(input("Введите год: "))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

is_year_leap()

#  Определение функции вычисления количества дней в месяце
def days_in_month(year, month):
    year = int(input("Введите год: "))
    month = int(input("Введите номер месяца: "))
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print(31)
    elif month==4 or month==6 or month==9 or month==11:
        print(30)
    elif month==2 and year==is_year_leap(year):
        print(29)
    elif month==2 and year!=is_year_leap(year):
        print(28)
    else:
        print("Такого месяца нет")

days_in_month

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end = "")
    results = is_year_leap(yr)
    if results == test_results[i]:
        print("OK")
    else:
        print("Failed")
