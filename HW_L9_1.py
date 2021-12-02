#########################
#Author: Kuleshova Yana
#Date: 02/12/2021
#Task: HW to L9_1
#########################

class Queue:
    def __init__(self):
        self.__stk = [] # создаем пустой список

    def put(self, elem):
        self.__stk.insert(0, elem) # в начало списка добавляем элемент
        return self.__stk

    def get(self):
        elem = self.__stk[-1] # задаем переменной последний элемент списка
        del self.__stk[-1] # удаляем последний элемент списка
        return elem # возвращаем последний элемент списка


que = Queue()

que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")