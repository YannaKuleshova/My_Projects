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