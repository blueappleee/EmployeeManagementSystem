from Data_Objects.Employee import Employee
from Data_Objects.SysAdmin import SysAdmin
from Data_Objects.Team import Team
from Data_Objects.Project import Project
from Persistence.AdminPersistenceService import AdminPersistenceService

"""
Admin Controller that Admin Interface will call for logic of process
"""
class AdminController(EmployeeController):
    Employee_rules = {'employeeID':'fixed', 'teamID':'fixed', 'managerID':'fixed', 
    'password':32, 'empType':3, 'fName':20, 'address':50,
    'lName': 20,'phoneNumber': 10,'workEmail': 40,'personalEmail':40,'directDepositNumber' :21,'ssn':9 , 'position': 40,
    'salary': 'int',                            
    'startDate': 'date','birthDate': 'date',
    'sickDaysRemaining' : 'sint','vacationDaysYearly': 'sint','vacationDaysRemaining' : 'sint', 'sickDaysYearly':'sint'}

    def __init__(self):
        super.__init__()

    """
    Search for admin by id to return
    """
    @staticmethod
    def searchAdminById(adminId) -> SysAdmin:
        validID = isfixed(adminId, "employeeID")
        if validID == True:
            self.dataobject=AdminPersistenceService.searchAdminById(adminId)
            return self.dataobject
        else:
            return validID

    """
    Set Employee Role
    """
    @staticmethod
    def setEmployeeRole(employeeId, role):
        validID = isfixed(employeeId, "employeeID")
        validRole = isfixed(role,"position")
        if validID == True and validRole == True:
            setRole=AdminPersistenceService.setEmployeeRole(employeeId, role)
            if setRole == 0:
                retstr = "employee with ID: " + employeeId + " not found"
                return retstr
            else
                return f'Success attribute position has been modified!'
        else if validID != True and validRole != True:
            return (validID,validRole)
        else if validID != True:
            return validID
        else:
            return validRole
        
    """
    Register new Employee
    """
    @staticmethod
    def registerNewEmployee(employee: Employee):
        AdminPersistenceService.registerNewEmployee(employee)
        pass

    """
    Make active employee inactive
    """
    @staticmethod
    def setEmployeeInactive(employeeId):
        validID=isfixed(employeeId, "employeeID")
        if validID == True:
            setInactive = AdminPersistenceService.setEmployeeInactive(employeeId)
            if setInactive[2] == 0:
                retstr = "employee with ID: " + employeeId + " not found"
                return retstr
            else:
                return f'Success employee has been set Inactive!'
        else:
            return validID
        pass

    """
    Assign a manager to a team
    """
    @staticmethod
    def assignManagerToTeam(managerId, teamId):
        validID = isfixed(managerId, "employeeID")
        validTeam = isfixed(teamId,"teamID")
        if validID == True and validTeam == True:
            setTeam=AdminPersistenceService.assignManagerToTeam(managerId, teamId)
            if setTeam[0] == 0 or setTeam[1] == 0 or setTeam[2] == 0 or setTeam[3] == 0:
                retstr = "employee with ID: " + employeeId + " not found"
                return retstr
            else
                return f'Success manager has been assigned to team!'
        else if validID != True and validTeam != True:
            return (validID,validTeam)
        else if validID != True:
            return validID
        else:
            return validTeam
        
    """
    Create team with data stored in Team object
    """
    @staticmethod
    def createTeam(team: Team):
        AdminPersistenceService.createTeam(team)
        pass

    """
    Create project with data stored in Project object
    """
    @staticmethod
    def createProject(project: Project):
        AdminPersistenceService.createProject(project)
        pass