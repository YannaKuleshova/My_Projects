#########################
#Author: Kuleshova Yana
#Date: 25/11/2021
#Task: 6_1
#########################

import math
import sys
import platform

# Определение версий
def determ_version():
    option = int(input('''
    Выбери что хочешь определить:   

    1 - Версию Python   
    2 - Версию ОС   
    3 - Версию процессора 

    Твой выбор: ''')) 
    
    # Определение версии Python
    if option == 1:
        print(platform.python_implementation() + ' ' + platform.python_version())
     # Определение ОС и ее версии
    elif option == 2:
        print(platform.system() + ' ' + platform.version())
    # Определение пропускной способности ПК
    else:
        print(platform.machine())

determ_version()

def determ_massege():

    if platform.system() == 'Linux':
        print(platform.system(), ' - Wow, your makin a hacker!')
    elif platform.machine() == 'AMD64':
        print(platform.machine(), ' - Not bad!')
    else: 
        print(platform.system(),' - Good!')

determ_massege()

def exit_func():
    while True:
        word =  input("Enter 'exit' for Break:")
        if word == 'exit':
            break

exit_func()