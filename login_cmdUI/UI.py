from abc import ABC, abstractmethod
import mysql.connector
import signal,  sys




class UI_generator():#a factory for creating different(access level) UI
    def generate(self, level, uid):
        generator = get_generator(level)
        return generator(uid)

def get_generator(level):
    if level == 'E':
        return generate_employeeUI
    elif level == 'M':
        return generate_managerUI
    elif level == 'A':
        return generate_adminUI
    else:
        print(f"Undefined access level, please contact system admin.")
        sys.exit(0)

def generate_employeeUI(uid):#employee factory
    return employee_UI(uid)
def generate_managerUI(uid):#manager factory
    return manager_UI(uid)
def generate_adminUI(uid):#admin factory
    return admin_UI(uid)

class general_UI(ABC):#abstract calss of differet UIs
    @abstractmethod
    def __init__(self):
        pass
    def search(type):
        pass
    def report_hours(none):
        pass
    def update_info(type):
        pass
    def get_query(sql):
        pass

class employee_UI(general_UI):
    def __init__(self,uid):
        self.query = {}
        self.uid = uid
    def search(type):
        {'uid':' ' ,'username':' '}
        if type == 'uid':
            searchkey = input('enter the userID:')
        elif type == 'username':
            searchkey = input('enter the username: ')
        else:
            print("invlid type, please enter again.")
            return
        #Left to implement...
        #connect to actor class use the *search* variable to search
    def update_info(type):
        #left to implement
        return
    def report_hours(none):
        #left to implement
        return
    def get_query(sql):
        return 
    def cmd_UI():
        while True:#ask for user input and map to the functions
            command = input("command: ")
            break
        return


    
class manager_UI(employee_UI):
    def assign_team(type):
        return
    def assign_project(type):
        return

class admin_UI(employee_UI):
    def register_employee(type):
        pass

