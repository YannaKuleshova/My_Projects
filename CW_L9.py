#########################
#Author: Kuleshova Yana
#Date: 02/12/2021
#Task: CW to L9
#########################

# CW
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)

obj = Sub("Andy")

print(obj)

# CW

import time

class Vehicle:
    def change_direction(self, left, on):
        pass
    
    def turn(self, left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)

class TrackedVehicle(Vehicle):
    def control_track(self, left, stop):
        pass

    def change_direction(self, left, on):
        control_track(left, on)

class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(self, left, on):
        turn_front_wheels(left, on)

# CW

class Top:
    def m_top(self):
        print("Top")
    
class Middle_Left(Top):
    def m_middle(self):
        print("Middle_left")

class Middle_Right(Top):
    def m_middle(self):
        print("Middle_right")

class Bottom(Middle_Left,Middle_Right):
    def m_bottom(self):
        print("Bottom")

obj = Bottom()
obj.m_bottom()
obj.m_middle()
obj.m_top()


# CW

class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name =  name

    def __str__(self):
        return "Hi, my name is " + self.name

class LabMouse(Mouse):
    pass

professor_mouse = LabMouse("Professor Mouser")
print(professor_mouse, Mouse.Population)

# CW

class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1

    def __str__(self):
        return self.breed + " says: Woof!"

class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don/'t run away, Little Lamb!"

class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister!"

rocky = GuardDog()
luna = SheepDog()
print(rocky)
print(luna)
print(issubclass(SheepDog,Dog), issubclass(SheepDog,GuardDog))
print(isinstance(rocky,GuardDog), isinstance(luna,GuardDog))