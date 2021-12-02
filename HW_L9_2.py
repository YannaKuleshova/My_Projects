#########################
#Author: Kuleshova Yana
#Date: 02/12/2021
#Task: HW to L9_2
#########################

class Pizza():
    def __init__(self):
        self.pizza = pizza
        self.cheese = cheese

    def make_pizza(self,pizza,cheese): # функция готовки пиццы
        if pizza not in ['margarita','capricciosa','calzone']: # если пицца выбрана не из меню
            raise PizzaError
        if cheese > 100: # если сыра больше 100 гр, выдает ошибку
            raise TooMuchCheeseError
        print("Pizza ready!") # если без ошибок, выдает сообщение, что пицца готова

class PizzaError(Exception): # создаем класс обработки ошибок
    def __init__(self,pizza):
        Exception.__init__(self)
        self.pizza = pizza
        print('No such pizza on the menu:', pizza)

class TooMuchCheeseError(PizzaError): # создаем класс обработки ошибки - много сыра
    def __init__(self,pizza,cheese):
        PizzaError.__init__(self,pizza)
        self.cheese = cheese
        print('Too much cheese: ', cheese)

pizza_obj = Pizza()

for (pizza, cheese) in [('calzone', 0), ('margarita', 110), ('mafia', 20)]: #  обработка ошибок
    try:
        pizza_obj.make_pizza(pizza,cheese)
    except TooMuchCheeseError as tmce: 
        print(tmce, ':', tmce.cheese) # вывод сообщения, если много сыра 
    except PizzaError as pe: 
        print(pe, ':', pe.pizza) # вывод сообщения если пиццы нет в меню
            
