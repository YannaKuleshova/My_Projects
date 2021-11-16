magic_numbers = 8
number = int(input("Enter a number: "))

# Check the number entered by the user 
# is the same as the number picked by the magician
while number != magic_numbers:
    if number != magic_numbers:
        print("Ha ha! You're stuck in my loop!")
        number = int(input("Enter a number again: "))
    else:    
        break
print("Well done, muggle! You are free now.")