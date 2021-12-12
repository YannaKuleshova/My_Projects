#########################
# Author: Kuleshova Yana
# Name_project: ToDo List
# Date: 12/12/2021
# Task: HW to L13
#########################

import sqlite3
import logging
import json

# Класс обарботки ошибок имени задачи.
class NameExc(Exception):
    def __init__(self, head="TDTaskNameError", mess="Bad name!"):
       super().__init__(mess)
       self.head = head
       self.mess = mess

# Класс обарботки ошибок приоритета задачи.
class PriorExc(NameExc):
    def __init__(self, head="TDTaskPriorityError", mess="Bad priority!"):
        super().__init__(mess)
        self.head = head
        self.mess = mess

# Класс обарботки ошибок Id задачи.
class IdExc(PriorExc):
    def __init__(self, head="TDTaskIdError", mess="Bad Id!"):
        super().__init__(mess)
        self.head = head
        self.mess = mess

# Класс формирования ToDo List.
class Todo:
    # Функция инициализации класса.
    def __init__(self):
        self.conn = sqlite3.connect('D:/PYTHON/My_Projects__/todo.db')
        #self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    # Функция создания таблицы задач в БД с колонками ID, NAME and PRIORITY.
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
            ); ''')
    
    # Функция добавления задачи в БД.
    def add_task(self):
        # Ввод пользователем имени задачи для добавления.
        task_name = input('Enter task name: ')
        # Если ничего не введдено, сообщение об ошибке.
        if len(task_name) == 0 or task_name.isspace():
            raise NameExc
        # Переменная поиска имени задачи в таблице.
        res = self.find_task(task_name) 

        if res == None:
            pass
        else:
            # Если задача уже существует, то сообщение об ошибке.
            raise NameExc(mes='Already have!')

        # Ввод пользователем приоритета задачи.
        priority = int(input('Enter priority: '))
        # Если приоритет меньше 1, сообщение об ошибке.
        if priority < 1: 
            raise PriorExc

         # Создание записи задачи в БД.
        self.c.execute('''INSERT INTO tasks (name, priority) VALUE (?,?)''', (task_name, priority))
        self.conn.commit()

    # Функция поиска задачи в БД.
    def find_task(self, task_name):
        self.task_name = task_name
        find = False

        # Выборка в БД по всем полям.
        que = '''SELECT id, name, priority FROM tasks;'''
        rows = self.c.execute(que)

        # Поиск по всем строкам.
        for row in rows:
            # Если задача в БД найдена, возвращает задачу.
            if row[1] == self.task_name:
                find = True
                return row
        # Если задача в БД не найдена - возвращает ничего.
        if not find:
            return None
    
    # Функция изменения приоритета задачи в БД.
    def change_priority(self):
        # Ввод пользователем желаемого приоритета.
        priority = int(input('Enter preferable priority: '))
        if priority < 1:
            raise PriorExc
        # Ввод пользователем ID.
        numid = int(input('Enter id: '))
        if numid < 1:
            raise IdExc

        # Обновление записи задачи в БД.
        self.c.execute('''UPDATE tasks SET priority = ? WHERE id = ?;''', (priority, numid))
        self.conn.commit()

    # Функция удаления задачи.
    def delete_task(self):
        # Ввод пользователем ID задачи для удаления.
        numid = int(input('Enter Id which you want to delete: '))
        # Если ID меньше 1, выводит ошибку.
        if numid < 1: 
            raise IdExc
        # Удаление записи задачи в БД.
        self.c.execute('''DELETE FROM tasks WHERE id = ?''', (numid,))
        self.conn.commit()

    # Функция отображения всех задач.
    def show_task(self): 
        print("Сейчас покажу все задачи: ")
        print("ID  |  Task name  |  Priority")
        # Выборка задач в БД по всем полям.
        for row in self.c.execute('''SELECT * FROM tasks;'''):
            #self.conn.commit()
            print(row)



#-------------JSON-------------
   
class MyEncoder(json.JSONEncoder):
    def default(self, w):
        # Проверка подкласса на принадлежность классу.
        if isinstance(w, Todo.show_task):
            # Возвращает словарь.
            return w.__dict__
        else:
            raise TypeError(w.__class__.__name__ + 'is not JSON')


class MyDecoder(json.JSONDecoder):
    # Инициализация класса.
    def __init__(self): 
        json.JSONDecoder.__init__(self, object_hook = self.decode_who)

    def decode_who(self):
        with open("D:/PYTHON/My_Projects__/result.json", "w") as wr_file:
            json.dumps(Todo.show_task, wr_file)
    
def json_show():
    json_str = json.dumps(MyEncoder.default)
    json.loads(json_str, cls = MyDecoder)    

#---------------------------


# Классу ToDo задаем переменную.
app = Todo()


# Функция создания меню для выбора действия пользователем.
def menu_controller (put = 0):

    # Если пользователь ввел 1.
    if put == 1:
    
    # Обработка ошибок для функции show task service.
        try:
            app.show_task()
        except NameExc as e:
            print(e.mess)
        except:
            print('Something goes badly!')
        else:
            print('All right!')
        finally:
            print('...')
    
    # Если пользователь ввел 2.
    elif put == 2:

    # Обработка ошибок для функции add task service.
        try:
            app.add_task()
        except NameExc as e:
            print(e.mess)
        except PriorExc as e:
            print(e.mess)
        except:
            print('Something goes bady :((')
        else:
            print('The task was added successfully')
        finally:
            print('...')
    
    # Если пользователь ввел 3.
    elif put == 3:

    # Обработка ошибок для функции update priority.
        try:
            app.change_priority()
        except PriorExc as e:
            print(e.mess)
        except IdExc as e:
            print(e.mess)
        except:
            print('Something goes badly!')
        else:
            print('The priority was update.')
        finally:
            print('...')

    # Если пользователь ввел 4.
    elif put == 4:

    # Обработка ошибок для функции delete task service.
        try:
            app.delete_task()
        except IdExc as e:
            print(e.mess)
        except:
            print('Something goes badly!')
        else:
            print('The task was deleted successfully.')
        finally:
            print('...')

    # Если пользователь ввел 5 - выход из программы.
    elif put == 5:
        exit

    else:
        pass

# Цикл выбора меню для ввода.
while True:
    print('''
    1. Show task
    2. Add task
    3. Change Priority
    4. Delete task
    5. Exit
    ''')
                
    try:
        put = int(input('Put what you want: 1 or 2 or 3 or 4 or 5: '))
        if put == 5:
            menu_controller(put)
            break
    except:
        print('Bad operation')
    else:
        if put in [1, 2, 3, 4]:
            menu_controller(put)

# Logging
import logging

# Формат вывода текста в лог-файле.
FORMAT = '%(name)s:\n%(levelname)s:\n%(asctime)s' 

logger = logging.getLogger(__name__)

handler = logging.FileHandler('D:/PYTHON/My_Projects__/ToDoList.log', mode = 'w')
handler.setLevel(logging.CRITICAL)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.critical('CRITICAL message')
logger.error('ERROR message')
logger.warning('WARNING message')
logger.info('INFO message')
logger.debug('DEBUG message')