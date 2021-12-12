#########################
#Author: Kuleshova Yana
#Date: 09/12/2021
#Task: HW to L12_3
#########################

import csv
from os import name

class PhoneContact:
    # Функция инициализации   
    def __init__(self, name, phone):
        super().__init__(name, phone)
        self.name = name
        self.phone = phone

class Phone(PhoneContact):
    # Функция инициализации 
    def __init__(self):
        super().__init__(name, phone)
        #PhoneContact.name = name
        #PhoneContact.phone = phone
        self.contacts = [] # Создаем пустой список, куда будем писать из файла

    # Функция чтения из файла
    def load_contacts_from_csv(self, file):
        with open(file, newline = '') as csvfile:
            fieldnames = ['Name', 'Phone']
            reader = csv.DictReader(csvfile, fieldnames)

            for row in reader:
                self.contacts.append(PhoneContact(row['Name'], row['Phone']))
    
    # Функция поиска контакта
    def search_contacts(self, phrase):
        self.phrase = phrase
        count = 0
        for contact in self.contacts:
            if phrase.lower() in contact.name.lower() \
                or phrase in phone:
                print('{0} {1}'.format(contact.name, contact.phone))
                count += 1
            if count == 0:
                print('No contact found!')

phone = Phone()

phone.load_contacts_from_csv('D:/PYTHON/My_Projects__/contacts.csv')

phrase = input('Search contacts: ')
phone.search_contacts(phrase)