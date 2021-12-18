#########################
#Author: Kuleshova Yana
#Date: 06/12/2021
#Task: CW to L10
#########################

# CW
# Считаем количество букв в файле
from os import strerror

try:
    cnt = 0 # по умолчанию ноль символов
    s = open('text.txt', 'rt') # открываем файл для чтения
    ch = s.read(1) # задаем переменную для считывания текста
    while ch != '': # запускаем цикл считывания, если символ не пусто
        print(ch, end = '') # печатаем текст разделяя пробелами
        cnt += 1 # плюсуем количество символов
        ch = s.read(1) # читаем следующий символ
    s.close() # закрываем файл
    print('\n\nCharacters in file:', cnt) # печатаем количество символов в файле
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# CW
# Тоже самое, только построчно

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt') 
    line = s.readline() 
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end = '') 
            ccnt += 1 
        line = s.readline() 
    s.close() 
    print('\n\nCharacters in file:', ccnt)
    print('Lines in line: ', lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# CW
from os import strerror

try:
    ccnt = lcnt = 0
    for line in open('text.txt', 'rt'):
        lcnt += 1 
        for ch in line:
            print(ch, end = '') 
            ccnt += 1 
    print('\n\nCharacters in file:', ccnt)
    print('Lines in line: ', lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# CW

from os import strerror

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        s = 'line #' + str(i + 1) + '\n'
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# CW

from os import strerror

try:
    i = 0
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        fo.write('line #' + str(i + 1) + '\n')
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


# CW
from os import strerror

srcname = input('Enter the source file name: ')
try:
    src = open(srcname, 'rb')
except IOError as e:
    print('Cannot open the source file: ', strerror(e.errno))
    exit(e.errno)

dstname = input('Enter the destinacion file name: ')
try:
    dst = open(dstname, 'wb')
except IOError as e:
    print('Cannot create the destination file: ', strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print('Cannot create the destination file: ', strerror(e.errno))
    exit(e.errno)

print(total, 'byte(s) succesfully written')
src.close()
dst.close()


# CW
from os import strerror

# WRITE
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))

# READ
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close

    for b in data:
        print(hex(b), end = '')

except IOError as e:
    print('I/O error occurred: ', strerror(e.errno))
