#########################
#Author: Kuleshova Yana
#Date: 30/11/2021
#Task: HW to L8_1
#########################


class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val    

class CountingStack(Stack):
    __counter = 0
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_counter(self):
        return CountingStack.__counter

    def push(self, val):
        self.__sum += val
        CountingStack.__counter += 1
        Stack.push(self, val)

stk = CountingStack()

for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())