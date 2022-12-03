from Data_Objects.Employee import Employee
from Data_Objects.SysAdmin import SysAdmin
from Data_Objects.Team import Team
from Data_Objects.Project import Project
from Business_Logic import EmployeeController as employeeController
from Persistence.AdminPersistenceService import AdminPersistenceService

"""
Admin Controller that Admin Interface will call for logic of process
"""
class AdminController(employeeController.EmployeeController):
    Employee_rules = {'employeeID':'fixed', 'teamID':'fixed', 'managerID':'fixed', 
    'password':32, 'empType':3, 'fName':20, 'address':50,
    'lName': 20,'phoneNumber': 10,'workEmail': 40,'personalEmail':40,'directDepositNumber' :21,'ssn':9 , 'position': 40,
    'salary': 'int',                            
    'startDate': 'date','birthDate': 'date',
    'sickDaysRemaining' : 'sint','vacationDaysYearly': 'sint','vacationDaysRemaining' : 'sint', 'sickDaysYearly':'sint'}

    def __init__(self):
        super().__init__()
        
    fixed_tp_length = {"projectID":8}
    max_tp_length = {"projectName":20, "projectStatus":20, "teamName":20}
    
    @staticmethod
    def isfixedNULL(input,type):
        fixLength = employeeController.EmployeeController.fixed_length[type]
        if fixLength == len(input) or input is None or input=="NULL": return True
        return f'Error: wrong attribute({type}) format. Must be exactly{fixLength}.'
    
    @staticmethod    
    def isMaxNULL(input,type):
        fixLength = AdminController.Employee_rules[type]
        if fixLength >= len(input) or input is None or input=="NULL": return True
        return f'Error: wrong attribute({type}) format. Must be up to{fixLength}.'
    
    @staticmethod    
    def isMax(input,type):
        fixLength = AdminController.Employee_rules[type]
        if fixLength >= len(input) or input is None or input=="NULL": return True
        return f'Error: wrong attribute({type}) format. Must be exactly{fixLength}.'

    @staticmethod
    def isfixedTP(input,type):
        fixLength = AdminController.fixed_tp_length[type]
        if fixLength == len(input): return True
        return f'Error: wrong attribute({type}) format. Must be exactly{fixLength}.'
        
    @staticmethod    
    def isMaxTPNULL(input,type):
        maxLength = AdminController.max_tp_length[type]
        if maxLength >= len(input) or input is None or input=="NULL": return True
        return f'Error: wrong attribute({type}) format. Must be up to {maxLength}.'
    
    @staticmethod    
    def isMaxTP(input,type):
        maxLength = AdminController.max_tp_length[type]
        if maxLength >= len(input): return True
        return f'Error: wrong attribute({type}) format. Must be up to {maxLength}.'
        
    """
    Search for admin by id to return
    """
    @staticmethod
    def searchAdminById(adminId) -> SysAdmin:
        validID = employeeController.EmployeeController.isfixed(adminId, "employeeID")
        if validID == True:
            AdminController.dataobject=AdminPersistenceService.searchAdminById(adminId)
            return AdminController.dataobject
        else:
            return validID

    """
    Set Employee Role
    """
    @staticmethod
    def setEmployeeRole(employeeId, role):
        validID = employeeController.EmployeeController.isfixed(employeeId, "employeeID")
        validRole = employeeController.EmployeeController.isfixed(role,"empType")
        if validID == True and validRole == True:
            setRole=AdminPersistenceService.setEmployeeRole(employeeId, role)
            if setRole == 0:
                retstr = "employee with ID: " + employeeId + " not found"
                return retstr
            else:
                return f'Success attribute role has been modified!'
        elif validID != True and validRole != True:
            return (validID,validRole)
        elif validID != True:
            return validID
        else:
            return validRole
        
    """
    Register new Employee
    """
    @staticmethod
    def registerNewEmployee(employee: Employee):
        attrValid ={"employeeID": employeeController.EmployeeController.isfixed(employee.employeeId, "employeeID")}
        #attrValid = {"employeeID": employeeController.EmployeeController.isfixed(employee.employeeId, "employeeID"), "password": AdminController.isMax(employee.password, "password"), "empType": employeeController.EmployeeController.isfixed(employee.empType, "empType"), "teamID": AdminController.isfixedNULL(employee.teamID, "teamID"), "managerID": AdminController.isfixedNULL(employee.managerId, "employeeID"), "fName": AdminController.isMax(employee.fName, "fName"), "lName": AdminController.isMax(employee.lName, "lName") , "salary": employeeController.EmployeeController.isint(employee.salary, "salary"), "position":AdminController.isMax(employee.position,"position"), "startDate": employeeController.EmployeeController.isdate(employee.startDate, "startDate"), "birthDate":employeeController.EmployeeController.isdate(employee.birthDate, "birthDate"), "sickDaysYearly": employeeController.EmployeeController.issint(employee.sickDaysYearly, "sickDaysYearly"), "sickDaysRemaining":(employeeController.EmployeeController.issint(employee.sickDaysRemaining, "sickDaysRemaining") or is None) , "vacationDaysYearly":(employeeController.EmployeeController.issint(employee.vacationDaysYearly, "vacationDaysYearly") or is None),    "vacationDaysRemaining":employeeController.EmployeeController.issint(employee.vacationDaysRemaining, "vacationDaysRemaining"), "address":AdminController.isMaxNULL(employee.address, "address"), "phoneNumber":AdminController.isfixedNULL(employee.phoneNumber,"phoneNumber"), "workEmail":, "personalEmail": AdminController.isMaxNULL(employee.personalEmail, "personalEmail"), "directDepositNumber": employeeController.EmployeeController.isfixed(employee.directDepositNumber, "directDepositNumber"), "ssn": employeeController.EmployeeController.isfixed(employee.ssn, "ssn")}
        if (all(value==True for value in attrValid.values())):
            AdminPersistenceService.registerNewEmployee(employee)
            return f'Success employee has been added!'
        else:
            return 'Invalid attribute provided'
        

    """
    Make active employee inactive
    """
    @staticmethod
    def setEmployeeInactive(employeeId):
        validID=employeeController.EmployeeController.isfixed(employeeId, "employeeID")
        if validID == True:
            setInactive = AdminPersistenceService.setEmployeeInactive(employeeId)
            if type(setInactive) == list and any("mysql.connector.errors" in str(attr) for attr in setInactive): 
               return f'An error occurred setting the employee inactive due to an invalid value'
            elif type(setInactive) == list and setInactive[0] == 0:
                return f'Employee not found'
            elif type(setInactive) != list:
                return f'An error occurred setting the employee inactive due to an invalid value'
            else:
                return f'Success employee has been set Inactive!'

        else:
            return validID
        
    """
    Assign a manager to a team
    """
    @staticmethod
    def assignManagerToTeam(managerId, teamId):
        validID = employeeController.EmployeeController.isfixed(managerId, "employeeID")
        validTeam = employeeController.EmployeeController.isfixed(teamId,"teamID")
        if validID == True and validTeam == True:
            setTeam=AdminPersistenceService.assignManagerToTeam(managerId, teamId)
            if type(setTeam) == list and any("mysql.connector.errors" in str(attr) for attr in setTeam): 
               return f'An error occurred assigning the manager to team due to an invalid value'
            elif type(setTeam) == list and (setTeam[0] == 0 or setTeam[1] == 0 or setTeam[2] == 0 or setTeam[3] == 0):
                retstr = "employee with ID: " + employeeId + " not found"
                return retstr
            elif type(setTeam) != list:
                return f'An error occurred setting the manager to the team'
            else:
                return f'Success manager has been assigned to team!'
        elif validID != True and validTeam != True:
            return (validID,validTeam)
        elif validID != True:
            return validID
        else:
            return validTeam
        
    """
    Create team with data stored in Team object
    """
    @staticmethod
    def createTeam(team: Team):
        # create isFixed team and is MAx team
        if employeeController.EmployeeController.isfixed(team.teamId, "teamID") != True:
            return f'Invalid teamID. Input must be 4 characters'
            
        if team.managerId is not None:
            if AdminController.isfixedNULL(team.managerId, "employeeID") != True:
                return f'Invalid ManagerID. Input must be 6 characters'
        else:
            team.managerId = "NULL"
            
        if team.projectId is not None:
            if AdminController.isfixedTPNULL(team.projectId, "projectID") != True:
                return f'Invalid projectID. Input must be 8 characters'
        else:
            team.projectId = "NULL"
            
        if team.name is not None:
            if AdminController.isMaxTPNULL(team.name, "teamName") != True:
                return f'Invalid team name. Input must be max 20 characters'
        else:
            team.name = "NULL"
        
        if team.teamMembers != []:
            for member in team.teamMembers:
                if employeeController.EmployeeController.isfixed(member, "employeeID") != True:
                    retStr = "Invalid employeeID for team member: " + member + " , employeeID must be 8 characters"
                    return retStr
        
        makeTeam=AdminPersistenceService.createTeam(team)
        if type(makeTeam) == list and any("mysql.connector.errors" in str(attr) for attr in makeTeam): 
           return f'An error occurred creating the team'
        elif type(makeTeam) != list:
            return f'An error occurred creating the team'
        else:
            return f'Success team has been created!'

    """
    Create project with data stored in Project object
    """
    @staticmethod
    def createProject(project: Project):
        if AdminController.isfixedTP(project.projectId, "projectID") != True:
            return f'Invalid projectID. Input must be 8 characters'
            
        if project.name is not None:
            if AdminController.isMaxTP(project.name, "projectName") != True:
                return f'Invalid project name. Input must be max 20 characters'
        else:
            project.name = "NULL"
            
        if project.currentTeamId is not None:
            if employeeController.EmployeeController.isfixed(project.currentTeamId, "teamID") != True:
                return f'Invalid team name. Input must be 4 characters'
        else:
            project.currentTeamId = "NULL"
            
        if project.status is not None:
            if AdminController.isMaxTP(project.status, "projectStatus") != True:
                return f'Invalid team name. Input must be max 20 characters'
        else:
            project.status = "NULL"
        
        makeProject=AdminPersistenceService.createProject(project)
        if type(makeProject) == list and any("mysql.connector.errors" in str(attr) for attr in makeProject): 
           return f'An error occurred creating the project'
        elif type(makeProject) != list:
            return f'An error occurred creating the project'
        else:
            return f'Success project has been created!'
