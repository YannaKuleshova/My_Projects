# example 1
numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num%2 == 0:
        print("The list contains an even number")
        break
else:
    print("The list doesn't contains an even number")


# example 2
count = 0
while count < 5:
    print(count, "is less then 5")
    count += 1
else:
    print(count, "is not less then 5")

# example 3
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("Else: ", i)



