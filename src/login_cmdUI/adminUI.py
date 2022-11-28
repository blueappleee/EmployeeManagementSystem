from generalUI import employee_UI
from generalUI import input_shoe_be_num
from Business_Logic.AdminController import AdminController

class admin_UI(employee_UI):
    def __init__(self, uid):
        super().__init__(uid)
        self.command_dict['role'] = self.assign_team
        self.command_dict['register'] = self.assign_project
        self.command_dict['inactive'] = self.correct_hours

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