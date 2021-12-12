#########################
#Author: Kuleshova Yana
#Date: 09/12/2021
#Task: HW to L12_1
#########################

import xml.etree.ElementTree as ET

# Создаем класс для конвертирования температур по формуле
class TemperatureConverter:
    def __init__(self, temperature_in_celsius):
        self.temperature_in_celsius = temperature_in_celsius

    def convert_celsius_to_fahrenhehit(self, temperature_in_celsius):
        return 9.0 / 5.0 * temperature_in_celsius + 32

# Создаем класс для чтения xml-файла
class ForecastXmlParser(TemperatureConverter):
    # Инициализация 
    def __init__(self, temperature_converter):
        super().__init__(self, temperature_converter)
        self.temperature_converter = temperature_converter
    
    # Считывание файла по заданным переменным
    def parser(self, file, temperature_converter):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            day = child.find('day').text
            temperature_in_celsius = int(child.find('temperature_in_celsius').text)
            temperature_in_fahrenheit = round/(temperature_converter.convert_celsius_to_fahrenhehit(temperature_in_celsius), 1)
            print('{0}: {1} Celsius, {2} Fahrengeit'.format(day, temperature_in_celsius, temperature_in_fahrenheit))

temperature_conv = TemperatureConverter()

forecast_xml_parser = ForecastXmlParser(temperature_conv)
forecast_xml_parser.parser('D:/PYTHON/My_Projects__/forecast.xml')