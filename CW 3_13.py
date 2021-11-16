larger_number = -999999999
counter = 0

number = int(input("Enter a number or type -1 to end program:"))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > larger_number:
        larger_number = number
    number = int(input("Enter a number or type -1 to end program:"))

if counter:
    print("The largest number is", larger_number)
else:
    print("You haven't entered any number.")
