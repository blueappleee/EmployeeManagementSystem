from generalUI import employeeUI
from generalUI import input_shoe_be_num
from Business_Logic.AdminController import AdminController
from Data_Objects.Employee import Employee
from Data_Objects.Team import Team
from Data_Objects.Project import Project
import hashlib

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
        everything=everything.replace(' ','')
        everything=everything.split(',')
        result=[None if v is None or v == '' else v for v in everything]
        if len(everything) != 19:
            print("Wrong number of attribute, make sure to write (, ,) for a null input")
            return
        msg = AdminController.registerNewEmployee(Employee(result[0], hashlib.md5(result[1]).hexdigest(), result[2], None, None, result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12], result[13], result[14], result[15], result[16], result[17], result[18]))
        print(msg)

    """
    Register new Team
    """    
    def registerNewTeam(self, none):
        print("Register everything, seperate by comma(,). In the order of teamID, teamManagerID, teamName\n")
        everything = input("")
        everything=everything.replace(' ','')
        everything=everything.split(',')
        result=[None if v is None or v == '' else v for v in everything]
        if len(everything) != 3:
            print("Wrong number of attribute, make sure to write (, ,) for a null input")
            return
        msg = AdminController.createTeam(Team(result[0], [], result[1], None, result[2]))
        print(msg)

    """
    Register new Team
    """    
    def registerNewProject(self, none):
        print("Register everything, seperate by comma(,). In the order of projectID, projectName, currentTeamID, projectStatus\n")
        everything = input("")
        everything=everything.replace(' ','')
        everything=everything.split(',')
        result=[None if v is None or v == '' else v for v in everything]
        if len(everything) != 4:
            print("Wrong number of attribute, make sure to write (, ,) for a null input")
            return
        msg = AdminController.createProject(Project(result[0],result[1],result[2],result[3]))
        print(msg)
	
    """
    Assign a manager to a team
    """    
    def assignMtoT(self, none):
        managerID = input("Enter the managerID: ")
        teamID = input("Enter the teamID: ")
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
report      *worktype = [W/S/V]                 To log your working hours
role        #employeeID                         To change the system access level for the employee
registere                                       To add a new employee to the system
registert                                       To add a new team to the system
registerp                                       To add a new project to the system
inactive    #employeeID                         To make an employee account inactive
assign                       			        To assign manager to a team
Type exit to logout
When type your command, Words start with * must be replaced by one of the keywords in []
Words start with # must be replaced by a valid number""")
