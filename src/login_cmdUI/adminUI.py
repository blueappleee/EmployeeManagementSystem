from generalUI import employeeUI
from generalUI import input_shoe_be_num
from Business_Logic.AdminController import AdminController

class adminUI(employeeUI):
    def __init__(self, uid):
        super().__init__(uid)
        self.command_dict['role'] = self.setEmployeeRole
        self.command_dict['register'] = self.registerNewEmployee
        self.command_dict['inactive'] = self.setInactive
        print(
"""You are loging in with SysAdmin priviliges, you can enter:
update      *attributes = [fName/lName/birthDate/phoneNumber/personalEmail]   To update your personal Info
report      *worktype = [something not sure]    To log your working hours
role        #employeeID                         To change the system access level for the employee
register                                        To add a new employee to the system
inactice    #employeeID                         To make an employee account inactive
Type exit to logout
When type your command, Words start with * must be replaced by one of the keywords in []
Words start with # must be replaced by a valid number""")
    """
    Register new Employee
    """
    def setEmployeeRole(self,employeeID):
        employeeID = input_shoe_be_num(employeeID)
        role = input("Specific the role: ")
        AdminController.setEmployeeRole(employeeID,role)

    """
    Register new Employee
    """    
    def registerNewEmployee(self, none):
        return
        #bunch of input to create a dataobject then pass to controller
        
    """
    Make active employee inactive
    """
    def setInactive(self,employeeID):
        employeeID = input_shoe_be_num(employeeID)
        AdminController.setEmployeeInactive(employeeID)