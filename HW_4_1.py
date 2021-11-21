# Определение функции
def calculate():
    chioce = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    x = int(input("Введите первое число: ")) # input first value
    y = int(input("Введите второе число: ")) # input second value
    if chioce == " + ":
        print(x, " + ", y, " = ")
        print(x + y)
    elif chioce == " - ":
        print(x, " - ", y, " = ")
        print(x - y)
    elif chioce == " * ":
        print(x, " * ", y, " = ")
        print(x * y)
    elif chioce == " / ":
        print(x, " / ", y, " = ")
        print(x / y)
    else:
        print('You have not typed a valid operator, please run the program again.')

# Вызов функции calculate() вне функции
calculate()

def plus(x,y):
    x = int(input("Введите первое число: ")) # input first value
    y = int(input("Введите второе число: ")) # input second value
    print(x, " + ", y, " = ")
    print(x + y)

plus()