# import calendar

def is_year_leap (year):
    year = int(input("Введите год: "))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

is_year_leap()

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