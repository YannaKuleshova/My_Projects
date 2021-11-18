list = []
n = int(input("Enter how many numbers do u want: "))

for i in range(n):
    number = int(input("Enter the number: "))
    list.append(number)

choice = int(input("Введите 1 для сортировки по возрастанию, 2 - по убыванию"))

if choice == 1:
# Сортировка по возрастанию
    swapped = True
    while swapped:
        swapped = False # no swaps so far
        for i in range(n):
            if list[i] > list[i + 1]:
                swapped = True # a swap occurred
                list[i], list[i + 1] = list[i + 1], list[i]
    print(list)   
else:
# Сортировка по убыванию
    while swapped:
        swapped = False # no swaps so far
        for i in range(n):
            if list[i] < list[i + 1]:
                swapped = True # a swap occurred
                list[i], list[i + 1] = list[i + 1], list[i]
    print(list)