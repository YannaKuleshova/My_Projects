#########################
#Author: Kuleshova Yana
#Date: 09/12/2021
#Task: HW to L12_4
#########################

import logging
import random

# Формат вывода текста в файле
FORMAT = '%(levelname)s - %(message)s' 

# Класс симуляции температур
class BatterySimulation:
    # Функция инициализации   
    def __init__(self, logger):
        self.logger = logger
    # Функция симуляции
    def simulate_last_hours(self):
        for minute in range(1, 60 + 1):
            temperature = random.randint(20, 40)

            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >= 30 and temperature <= 35:
                self.logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception('Temperature out of range.')

logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('D:/PYTHON/My_Projects__/battery_temperature.log', mode = 'w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

battery_simulation = BatterySimulation(logger)
battery_simulation.simulate_last_hours()


