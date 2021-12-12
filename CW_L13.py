#########################
#Author: Kuleshova Yana
#Date: 11/12/2021
#Task: CW to L13
#########################

# Class Work
import socket

server_addr = input('What server do you want to coonect to? ')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(b"GET / HTTP/1.1\r\nHost: " + \
          bytes(server_addr, 'utf8') + \
          b"\r\nConnection: close\r\n\r\n")   

reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close
print(repr(reply))

# Class Work
import json

electron = 1.602176620898e10-19
print(json.dumps(electron))

comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
print(json.dumps(comics))

my_list = [1, 2.34, True, "False", None, ['a', 0]]
print(json.dumps(my_list))

my_dict = {'me':"Python", 'pi': 3.141592653589,\
            'data':(1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))

# Class Work
import json

class Who:
    def __init__(self, name, age): # Инициализация класса
        self.name = name
        self.age = age

class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who): # Проверка подкласса на принадлежность классу
            return w.__dict__ # Возвращает словарь
        else:
            raise TypeError(w)

some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls = MyEncoder))


# Class Work
import json

class Who:
    def __init__(self, name, age): # Инициализация класса
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who): # Проверка подкласса на принадлежность классу
        return w.__dict__ # Возвращает словарь
    else:
        raise TypeError(w.__class__.__name__ + 'Is not JSON serializable')

def decode_who(w):
    return Who(w['name'], w['age'])


old_man = Who('Jane Doe', 23)
print(old_man)
json_str = json.dumps(old_man, default = encode_who)
print(json_str)
new_man = json.loads(json_str, object_hook=decode_who)
print(new_man)
print(type(new_man))
print(new_man.__dict__)


# Class Work
import json

class Who:
    # Инициализация класса.
    def __init__(self, name, age):
        self.name = name
        self.age = age

class MyEncoder(json.JSONEncoder):
    def default(self, w):
        # Проверка подкласса на принадлежность классу.
        if isinstance(w, Who):
            # Возвращает словарь.
            return w.__dict__
        else:
            raise self.default(self, w)

class MyDecoder(json.JSONDecoder):
    # Инициализация класса.
    def __init__(self): 
        json.JSONDecoder.__init__(self, object_hook = self.decode_who)

    def decode_who(self, d):
        return Who(**d)

some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls = MyEncoder)
new_man = json.loads(json_str, cls = MyDecoder)

print(type(new_man))
print(new_man.__dict__)