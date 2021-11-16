numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num%2 == 0:
        print("The list contains an even number")
        break
else:
    print("The list doesn't contains an even number")