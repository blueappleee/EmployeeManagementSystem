import sys
sys.path.append('../src')
from generalUI import employeeUI
from generalUI import input_shoe_be_num
from Business_Logic.AdminController import AdminController
from Data_Objects.Employee import Employee

class adminUI(employeeUI):
    def __init__(self, uid):
        super().__init__(uid)
        self.command_dict['role'] = self.setEmployeeRole
        self.command_dict['registere'] = self.registerNewEmployee
        self.command_dict['inactive'] = self.setInactive
        self.command_dict['registerp'] = self.registerNewProject
        self.command_dict['registert'] = self.registerNewTeam
        self.command_dict['assign'] = self.assignMtoT
        
    """
    Register new Employee
    """
    def setEmployeeRole(self,employeeID):
        employeeID = input_shoe_be_num(employeeID,'employeeID')
        role = input("Specific the role(mng/reg/adm): ")
        roles = {'mng': 1,'reg':1, 'adm':1}
        while role not in roles:
            role = input("Enter a valid role(mng/reg/adm): ")
        msg = AdminController.setEmployeeRole(employeeID,role)
        if isinstance(msg, str):
            print(msg)
            return
        print("Invalid ID")
            
		

    
        
    """
    Make active employee inactive
    """
    def setInactive(self,employeeID):
        employeeID = input_shoe_be_num(employeeID,'employeeID')
        msg = AdminController.setEmployeeInactive(employeeID)
        if isinstance(msg, str):
            print(msg)
            return
        print("Invalid ID")

    """
    Register new Employee
    """    
    def registerNewEmployee(self, none):
        print("""Register everything, seperate by comma(,). In the order of\n employeeID, password, empType, fname, lname, salary, position, startDate, birthDate,
sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn\n""")
        everything = input("")
        everything.replace(' ','')
        everything.split()
        if len(everything) != 19:
            print("Wrong number of attribute, make sure to write (, ,) for a null input")
            return
        msg = AdminController.registerNewEmployee(Employee(*everything))
        print(msg)

    """
    Register new Team
    """    
    def registerNewTeam(self, none):
        print("Register everything, seperate by comma(,). In the order of teamID, teamManagerID, teamName\n")
        everything = input("")
        everything.replace(' ','')
        everything.split()
        if len(everything) != 3:
            print("Wrong number of attribute, make sure to write (, ,) for a null input")
            return
        msg = AdminController.registerNewEmployee(Employee(*everything))
        print(msg)

    """
    Register new Team
    """    
    def registerNewProject(self, none):
        print("Register everything, seperate by comma(,). In the order of projectID, projectName, currentTeamID, projectStatus\n")
        everything = input("")
        everything.replace(' ','')
        everything.split()
        if len(everything) != 4:
            print("Wrong number of attribute, make sure to write (, ,) for a null input")
            return
        msg = AdminController.registerNewEmployee(Employee(*everything))
        print(msg)
	
    """
    Assign a manager to a team
    """    
    def assignMtoT(self, managerID):
        managerID = input_shoe_be_num(managerID,'teamID')
        teamID = input("Enter the teamID: ")
        teamID = input_shoe_be_num(teamID,'teamID')
        msg = AdminController.assignManagerToTeam(managerID,teamID)
        if isinstance(msg, str):
            print(msg)
            return
        print("Invalid teamID or managerID")
		
		
		
    def welcome(self,name):
        print(f'Hi, Admin {name}. Welcome!')
        print(
"""You are loging in with SysAdmin priviliges, you can enter:
update      *attributes = [fName/lName/birthDate/phoneNumber/personalEmail]   To update your personal Info
report      *worktype = [something not sure]    To log your working hours
role        #employeeID                         To change the system access level for the employee
registere                                       To add a new employee to the system
registert                                       To add a new team to the system
registerp                                       To add a new project to the system
inactice    #employeeID                         To make an employee account inactive
Type exit to logout
When type your command, Words start with * must be replaced by one of the keywords in []
Words start with # must be replaced by a valid number""")
