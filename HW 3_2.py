# Read four numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))

# Choose the max and min number
max_number = max(number4,number3, number2, number1)
min_number = min(number4,number3, number2, number1)

# Print the result
print("The max number is: ", max_number, type(max_number))
print("The min number is: ", min_number, type(min_number))