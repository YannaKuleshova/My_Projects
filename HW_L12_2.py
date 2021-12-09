#########################
#Author: Kuleshova Yana
#Date: 09/12/2021
#Task: HW to L12_2
#########################

import xml.etree.ElementTree as ET

# Создаем класс
class XmlTreeHelper:
    # Создаем функцию инициализации   
    def __init__(self, parent, tags):
        self.parent = parent
        self.tags = tags
    
    # Создаем функцию добавления тегов 
    def add_tags_with_text(self, parent, tags):
        elements = [] # создаем пустой список
        for tag in tags:
            element = ET.SubElement(parent, tag)
            element.text = tags[tag]
            elements.append(element)
        return elements

root = ET.Element('shop')
tree = ET.ElementTree(root)
tree.write('D:/PYTHON/My_Projects__/shop.xml', 'UTF-8', True)

category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})

product_1 = ET.SubElement(category, 'product', {'name': 'Good Morning Sunshine'})
product_2 = ET.SubElement(category, 'product', {'name': 'Spaghetti Veganietto'})
product_3 = ET.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})