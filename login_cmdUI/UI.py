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
    def search(self,type):
        pass
    def report_hours(self,none):
        pass
    def update_info(self,type):
        pass
    def get_query(self,sql):
        pass

class employee_UI(general_UI):
    def __init__(self,uid):
        self.query = {}
        self.uid = uid
        self.command_dict = {'search': self.search, 'update': self.update_info, 'report' : self.report_hours, }
        self.cmd_UI()
    def terminate(self,type):
        print("System terminates...")
        sys.exit(0)
    def search(self,type):
        keys = {'uid':' ' ,'username':' '}
        if type == 'uid':
            searchtype = 'uid'
            searchkey = input('enter the userID:')
        elif type == 'username':
            searchtype = 'username'
            searchkey = input('enter the username: ')
        else:
            print("invlid type, please enter again.")
            return
        keys[searchtype] = searchkey
        #using this to connect to deeper layer
        #Left to implement...
        #connect to actor class use the *search* variable to search
    def update_info(self,type):
        #left to implement
        return
    def report_hours(self,length):
        #left to implement
        return
    def get_query(self,sql):
        return
    def cmd_UI(self):
        while True:#ask for user input and map to the functions
            command = input("command: ").split()
            if(len(command) != 2):
                print('Invalid format, should be ***search [key_type = uid/usrname]***, and other stuffs dont know yet\n')
                continue
            if command[0] in self.command_dict:#map input commnad to command functions
                self.command_dict[command[0]](command[1])
            else:
                print('invalid command, you can choose ....... need to decide\n')
        


    
class manager_UI(employee_UI):
    def assign_team(self,type):
        return
    def assign_project(self,type):
        return

class admin_UI(employee_UI):
    def register_employee(self,type):
        pass

