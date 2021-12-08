#########################
#Author: Kuleshova Yana
#Date: 07/12/2021
#Task: HW to L11
#########################

import sqlite3

class NameExc(Exception):
    def __init__(self, head="TDTaskNameError", mess="Bad name!"):
        super().__init__(mess)
        self.head = head
        self.mess = mess

class PriorExc(NameExc):
    def __init__(self, head="TDTaskPriorityError", mess="Bad priority!"):
        super().__init__(mess)
        self.head = head
        self.mess = mess

class IdExc(PriorExc):
    def __init__(self, head="TDTaskIdError", mess="Bad Id!"):
        super().__init__(mess)
        self.head = head
        self.mess = mess

class Todo():
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    # Создание таблицы задач с колонками ID, NAME and PRIORITY в БД
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
            ); ''')
    
    # Добавление задачи
    def add_task(self, task_name):
        name = input('Enter task name: ') # Введите имя задачи
        if len(name) == 0 or name.isspace(): # Если имя пустое, сообщение об ошибке
            raise NameExc

        res = self.find_task(task_name) # переменная поиска задачи в таблице

        if res == None:
            pass
        else:
            raise NameExc(mes='This name already in task!') # Если задача уже существует, то сообщение ошибка

        priority = int(input('Enter priority: ')) # Введите приоритет задачи
        if priority < 1: # Если приоритет меньше 1, сообщение об ошибке
            raise PriorExc

        self.c.execute('''INSERT INTO task (name, priority) VALUE (?,?)''', (name, priority)) # создаем запись задачи в БД
        self.conn.commit()

    # Поиск задачи в БД
    def find_task(self, task_name):
        self.task_name = task_name
        find = False

        que = '''SELECT id, name, priority FROM task;''' # выборка в БД по всем полям
        rows = self.c.execute(que)

        for row in rows: # поиск по всем строкам
            if row[1] == self.task_name: # если задача найдена, возвращает задачу
                find = True
                return row

        if not find: # если нет - ничего
            return None
    
    # Отображение всех задач
    def show_task(self): 
        print("Сейчас покажу все задачи: ")
        print("ID  |  Task name  |  Priority")

        for row in self.c.execute('''SELECT * FROM task;'''): # выборка в Бд по всем полям
            print(row)
    
    # Удаление задачи
    def delete_task(self):
        numid = int(input('Enter id which you want to delete: ')) # Введите ID задачи, которую нужно удалить
        if numid < 1: # если ID меньше 1, выводит ошибку
            raise IdExc

        self.c.execute('''DELETE FROM task WHERE id = ?''', (numid,)) # удаление записи задачи в БД
        self.conn.commit()

    # Изменение приоритета задачи
    def change_priority(self):
        priority = int(input('Enter preferable priority: ')) 
        if priority < 1:
            raise PriorExc

        numid = int(input('Enter id: '))
        if numid < 1:
            raise IdExc

        que = '''UPDATE task SET priority = ? WHERE id = ?;'''
        self.c.execute('''UPDATE task SET priority = ? WHERE id = ?;''', (priority, numid))
        self.conn.commit()
 
app = Todo()

# Обработка выбора пользователя и ошибок
def menu_controller (put = 0):

    if put == 1:
    
    # show task service
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

    elif put == 2:

    # add task service
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
    
    elif put == 3:

    # update priority
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

    elif put == 4:

    # delete task service
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

    #elif put == 5:
        #app.exit()

    else:
        pass


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