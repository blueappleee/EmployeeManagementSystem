import sys,pyfiglet
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

class employeeUI(general_UI):
    def __init__(self,uid):
        self.query = {}
        self.uid = uid
        self.command_dict = {'update': self.update_info, 'report' : self.report_hours,'exit' : self.terminate }
        self.dataobject = None
        print(
"""You are loging in with regular employee priviliges, you can enter:
update  *attributes = [fName/lName/birthDate/phoneNumber/personalEmail]   To update your personal Info with specific attributes
report  *worktype = [something not sure]    To log your working hours with specific work type
When type your command, Words start with * must be replaced by one of the keywords in []
Type exit to logout""")
    def assignDataObject(self,data):
        self.dataobject = data
    def terminate(self,type):
        ascii_banner = pyfiglet.figlet_format("Bye!")
        print("System terminates...")
        print(ascii_banner)
        sys.exit(0)
    def update_info(self,attribute):
        while(True):
            try:
                getattr(self.dataobject,attribute)
                break
            except Exception:
                attribute = input('Enter an valid attribute in [fName/lName/birthDate/phoneNumber/personalEmail]: ')
        changed_attribute = input("changed value: ")
        setattr(self.dataobject, attribute, changed_attribute)
        #this line need fuether detailc for dataobject INFO
        msg = ec.EmployeeController.updateEmployeeInformation(attribute,self.dataobject)
        print(msg)
    def report_hours(self,worktype):
        workTime = input("Enter work hours: ")
        workTime = input_shoe_be_num(workTime)
        ec.EmployeeController.logWorkHours(self.dataobject,worktype,workTime)
        #left to implement
    def cmd_UI(self):
        while True:#ask for user input and map to the functions
            command = input("command: ").split()
            if len(command) == 0: continue
            if command[0] in self.command_dict:#map input commnad to command functions
                if len(command)>1:
                    param = command[1]
                else:
                    param = ' '
                self.command_dict[command[0]](param)
            else:
                print('invalid command, you can choose ....... need to decide\n')