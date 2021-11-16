odd_numbers = 0
even_numbers = 0

# Read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number!= 0:
    # Check if the number is odd
    if number % 2 == 1
        # Increate the odd_numbers counter.
        odd_numbers +=1
    else:
        # Increate the even_numbers counter.
        even_numbers  += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print result
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)