#########################
#Author: Kuleshova Yana
#Date: 30/11/2021
#Task: CW to L8
#########################

# CW
try:
    print('Let\'s try to do this')
    print('#'[2])
    print('We succeeded')
except:
    print('We failed')
print('We\'re done')

# CW
try:
    print('alpha'[1/0])
except ZeroDivisionError:
    print('zero')
except IndexError:
    print('Index')
except:
    print('some')

# CW
try:
    y = 1/0
except ZeroDivisionError:
    print("Oooooppsss....")

print("THE END.")

# CW
try:
    y = 1/0
except ArithmeticError:
    print("Oooooppsss....2")

print("THE END.2")

# CW
try:
    y = 1/0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

# CW
try:
    y = 1/0
except ArithmeticError:
    print("Arithmetic problem!")    
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")

# CW
def bad_fun(n):
    try:
        return 1/n
    except ArithmeticError:
        print("Arithmetic problem!")    
    return None

bad_fun(0)
print("THE END.")


# CW
def bad_fun1(n):
    return 1/n
try:
    bad_fun1(0)    
except ArithmeticError:
    print("What happened? An exception was raised!")    

print("THE END.")

# CW
def bad_fun(n):
    raise ZeroDivisionError

    try:
        bad_fun(0)
    except ArithmeticError:
        print("What happened? An error?")

print("THE END.")

# CW
def bad_fun(n):
    try:
        return n/0
    except:
        print("I did it again")
        raise

try:
    bad_fun(0)
except ArithmeticError:
    print("I see")

print("THE END.")


# CW
import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

#CW
try:
    print(1/0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")

#CW
try:
    print(1/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

#CW
def foo(x):
    assert x
    return 1/x

try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")

#CW
from math import exp, tan, radians
angle = int(input('Enter integral angle in degrees: '))

assert angle % 180 != 90
print(tan(radians(angle)))


#CW
from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print('Don\'t do that!')

# CW

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')

#CW
try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed')
    
