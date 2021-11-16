# Read four numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
elif number2 > number3:
    larger_number = number2
elif number3 > number4:
    larger_number = number3
else:
    larger_number = number4

# Print the result
print("The larger number is: ", larger_number)