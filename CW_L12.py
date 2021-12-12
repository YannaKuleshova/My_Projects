#########################
#Author: Kuleshova Yana
#Date: 09/12/2021
#Task: CW to L12
#########################

# Class Work
import xml.etree.ElementTree as ET

tree = ET.parse('D:/PYTHON/My_Projects__/books.xml')
root = tree.getroot()
print('The root tag is: ', root.tag)
print('The root has the following children: ')

for child in root:
    print(child.tag, child.attrib)

# Class Work
import xml.etree.ElementTree as ET

tree = ET.parse('D:/PYTHON/My_Projects__/books.xml')
root = tree.getroot()
print('My books:\n')
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author: ', book[0].text)
    print('Year: ', book[1].text, '\n')

# Class Work
import xml.etree.ElementTree as ET

tree = ET.parse('D:/PYTHON/My_Projects__/books.xml')
root = tree.getroot()
for book in root.findall('book'):
    print(book.get('title'))


# CW
import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logger = logging.getLogger()

logging.basicConfig(level=logging.CRITICAL, filename='D:/PYTHON/My_Projects__/prod.log',\
     filemode='a', format = FORMAT)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

# CW
import logging

#FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logger = logging.getLogger(__name__)

handler = logging.FileHandler('D:/PYTHON/My_Projects__/prod.log', mode='w')
handler.setLevel(logging.CRITICAL)

logger.addHandler(handler)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

# CW
import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logger = logging.getLogger(__name__)

handler = logging.FileHandler('D:/PYTHON/My_Projects__/prod.log', mode='w')
handler.setLevel(logging.CRITICAL)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

# CW
import configparser

config = configparser.ConfigParser

print(config.read('D:/PYTHON/My_Projects__/config.ini'))

print('Sections: ', config.sections(), '\n')

print('mariadb section: ')
print('Host: ', config.get('mariadb','host'))
print('Database: ', config.get('mariadb','name'))
print('Username: ', config.get('mariadb','user'))
print('Password: ', config.get('mariadb','password'), '\n')

print('redis section: ')
print('Host: ', config.get('redis','host'))
print('Port: ', int(config.get('redis','port')))
print('Database number: ', int(config.get('redis','db')))

print('Host: ', config.get(('mariadb','host')))