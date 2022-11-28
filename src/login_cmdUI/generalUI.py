import sys
from abc import ABC, abstractmethod
from Business_Logic import EmployeeController as ec

def input_shoe_be_num(string) -> int:
    while not string.isnumeric():
        string = input("enter an valid numer: ")
    return int(string)
"""
Parent abstract class for all UIs
"""
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
        self.dataobject = None
    def assignDataObject(self,data):
        self.dataobject = data
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
    def update_info(self,attribute):
        changed_attribute = input("changed value: ")
        self.dataobject.attribute =  attribute #this line need fuether detailc for dataobject INFO
        ec.EmployeeController.updateEmployeeInformation(self.dataobject)
        return
    def report_hours(self,worktype):
        workTime = input("Enter work hours: ")
        workTime = input_shoe_be_num(workTime)
        ec.EmployeeController.logWorkHours(self.dataobject,worktype,workTime)
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