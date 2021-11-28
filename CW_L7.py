#########################
#Author: Kuleshova Yana
#Date: 27/11/2021
#Task: CW to L7
#########################

# CW
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Uniiverse.')

# CW
temperature = float(input('Enter current temperature:'))

if temperature > 0:
    print('Above zero')
elif temperature < 0:
    print('Below zero')
else:
    print('Zero')

# CW
while True:
    try:
        number = int(input('Enter an integer number: '))
        print(number / 2)
        break
    except:
        print('Warning: the value entered is not a valid number. Try again ...')

# CW
while True:
    try:
        number = int(input('Enter an int number: '))
        print(5 / number)
        break
    except (ValueError, ZeroDivisionError):
        print('Wrong value or No division by zero rule broken')
    except:
        print('Sorry, something went wrong...')
