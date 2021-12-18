#########################
#Author: Kuleshova Yana
#Date: 18/12/2021
#Task: HW to L10
#########################

from os import strerror

try:
    count = 0
    win = open('D:/PYTHON/My_Projects__/text.txt')
    ch = win.read()  
    new_values = {}

    for i in ch.lower():
        if i in new_values.keys():
            new_values[i] += 1
        else:
            new_values[i] = 1
    
    for key, value in new_values.items():
        print(key, ' -> ', value, end = '\n')

except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))
finally:
    win.close()