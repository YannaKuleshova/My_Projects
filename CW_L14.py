#########################
#Author: Kuleshova Yana
#Date: 14/12/2021
#Task: CW to L14
#########################

# Class Work
import json
import xml.etree.ElementTree

from requests import exceptions

cars_for_sale = xml.etree.ElementTree.parse('D:/PYTHON/My_Projects__/cars.xml').getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print("\t\t", prop.tag, "=", prop.text, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
            print(' =', prop.text)
        print()


# Class Work

tree = xml.etree.ElementTree.parse('D:/PYTHON/My_Projects__/cars.xml')
cars_for_sale = tree.getroot()

for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale(car)
        break

new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_yaer').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
tree.write('D:/PYTHON/My_Projects__/new_cars.xml', method='')


# Class Work
import requests

reply = requests.get('http://localhost:3000', verify=False)

if reply.status_code == requests.codes.ok:
    print("ALL RIGHT ! ")
else:
    print("BAD ! ")

print(reply.status_code)
print(reply.headers)
print(reply.headers['Content - Type'])

print()
print(requests.codes.__dict__)


# Class Work - timeout
import requests

try:
    reply = requests.get('http://localhost:3000', timeout=1)
except requests.exceptions.Timeout:
    print('Sorry, MR...')
else:
    print('Here is your data')

try:
    reply = requests.get('https://vk.com', timeout=0.0000001)
except requests.exceptions.Timeout:
    print('Sorry, MR...')
else:
    print('Here is your data')

try:
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print('Noby\'s home, sorry!')
else:
    print('Everithing fine!')


# Class Work -- json -- GET (чтение данных).

import requests

key_names = ['id', 'brand', 'model', 'production_year', 'convertible']
key_widths = [10, 15, 10, 20, 15]

# Функция печати заголовка из файла.
def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end = '|  ')
    print()

# Функция печати "ничего"
def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end = '|  ')
    print()

# Функция печати данных из файла.
def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end = '|  ')
    print()

# Функция печати всего содержимого файла.
def show(json):
    # Отображение заголовка.
    show_head()
    # Если данные json в формате строк - вывод данных по умолчанию.
    if type(json) is list:
        for car in json:
            show_car(car)
    # Если данные json в формате словаря - вывод данных по json.
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()

try:
    reply = requests.get('http://localhost:3000/cars?_sort=production_year')
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        print("Server error")

# Class Work -- json -- POST (передача данных)

import requests
import json

h_close = {'Connection': 'Close'}
h_connect = {'Content-Type': 'application/json'}
new_car = { 'id': 10,
            'brand': 'VAZ',
            'model': '21063',
            'production_year': 1996,
            'convertible': False
            }
print(json.dumps(new_car))

try:
    reply = requests.post('http://localhost:3000/cars',\
                             headers=h_connect,
                             data=json.dumps(new_car))
    print("reply=" + str(reply.status_code))
    
    reply = requests.get('http://localhost:3000/cars/',\
                             headers=h_close)
except requests.RequestException:
    print("Communication error")
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server error")       

# Class Work -- json -- DELETE (удаление данных).

import requests
import json

h_close = {'Connection': 'Close'}
h_connect = {'Content-Type': 'application/json'}
new_car = { 'id': 6,
            'brand': 'Mercedes-Benz',
            'model': '300SL',
            'production_year': 1965,
            'convertible': True}
#print(json.dumps(new_car))

try:
    reply = requests.delete('http://localhost:3000/cars/1')
    print("res=" + str(reply.status_code))
    reply = requests.delete('http://localhost:3000/cars/2')
    print("res=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars/',\
                             headers=h_close)
except requests.RequestException:
    print("Communication error")
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server error")       


# Class Work -- json -- PUT (изменение данных), 
# (отправка запроса на поставку на сервер через http).

import requests
import json

h_close = {'Connection': 'Close'}
h_connect = {'Content-Type': 'application/json'}
new_car = { 'id': 6,
            'brand': 'Mercedes-Benz',
            'model': '300SL',
            'production_year': 1965,
            'convertible': True}
#print(json.dumps(new_car))

try:
    reply = requests.put('http://localhost:3000/cars/6',\
                             headers=h_connect,
                             data=json.dumps(new_car))
    print("res=" + str(reply.status_code))
    
    reply = requests.get('http://localhost:3000/cars/',\
                             headers=h_close)
except requests.RequestException:
    print("Communication error")
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server error")       

