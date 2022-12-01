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
        
    fixed_tp_length = {"projectID":8}
    max_tp_length = {"projectName":20, "projectStatus":20, "teamName":20}
    
    def isfixedNULL(input,type):
        fixLength = super().fixed_length[type]
        if fixLength == len(input) or if input is None or if input="NULL": return True
        return f'Error: wrong attribute({type}) format. Must be exactly{fixLength}.'
        
    def isMaxNULL(input,type):
        fixLength = super().Employee_rules[type]
        if fixLength >= len(input) or if input is None or if input="NULL": return True
        return f'Error: wrong attribute({type}) format. Must be up to{fixLength}.'
        
    def isMax(input,type):
        fixLength = super().Employee_rules[type]
        if fixLength >= len(input) or if input is None or if input="NULL": return True
        return f'Error: wrong attribute({type}) format. Must be exactly{fixLength}.'

    def isfixedTP(input,type):
        fixLength = self.fixed_tp_length[type]
        if fixLength == len(input): return True
        return f'Error: wrong attribute({type}) format. Must be exactly{fixLength}.'
        
    def isMaxTP(input,type):
        maxLength = self.max_tp_length[type]
        if maxLength >= len(input): return True
        return f'Error: wrong attribute({type}) format. Must be up to {maxLength}.'
        
    """
    Search for admin by id to return
    """
    @staticmethod
    def searchAdminById(adminId) -> SysAdmin:
        validID = super().isfixed(adminId, "employeeID")
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
        validID = super().isfixed(employeeId, "employeeID")
        validRole = super().isfixed(role,"position")
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
        attrValid = {"employeeID": super().isfixed(employee.employeeId, "employeeID"), "password": self.isMax(employee.password, "password"), "empType": super().isfixed(employee.empType, "empType"), "teamID": self.isfixedNULL(employee.teamID, "teamID"),
        "managerID": self.isfixedNULL(employee.managerId, "employeeID"), "fName": self.isMax(employee.fName, "fName"), "lName": self.isMax(employee.lName, "lName") , "salary": super().isint(employee.salary, "salary"), "position":self.isMax(employee.position,"position"), "startDate": super().isdate(employee.startDate, "startDate"), 
        "birthDate":super().isdate(employee.birthDate, "birthDate"), "sickDaysYearly": super().issint(employee.sickDaysYearly, "sickDaysYearly"), "sickDaysRemaining":(super().issint(employee.sickDaysRemaining, "sickDaysRemaining") or is None) , "vacationDaysYearly":(super().issint(employee.vacationDaysYearly, "vacationDaysYearly") or is None),
        "vacationDaysRemaining":super().issint(employee.vacationDaysRemaining, "vacationDaysRemaining"), "address":self.isMaxNULL(employee.address, "address"), "phoneNumber":self.isfixedNULL(employee.phoneNumber,"phoneNumber"),
        "workEmail":, "personalEmail": self.isMaxNULL(employee.personalEmail, "personalEmail"), "directDepositNumber": super().isfixed(employee.directDepositNumber, "directDepositNumber"), "ssn": super().isfixed(employee.ssn, "ssn")}
        
        if all(value==True for value in attrValid.values()):
            AdminPersistenceService.registerNewEmployee(employee)
            return f'Success employee has been added!'
        else:
            return 'Invalid attribute provided'
        

    """
    Make active employee inactive
    """
    @staticmethod
    def setEmployeeInactive(employeeId):
        validID=super().isfixed(employeeId, "employeeID")
        if validID == True:
            setInactive = AdminPersistenceService.setEmployeeInactive(employeeId)
            if setTeam.contains("mysql.connector.errors"): 
                return f'An error occurred setting the employee inactive due to an invalid value'
            else if setInactive[2] == 0:
                retstr = "employee with ID: " + employeeId + " not found"
                return retstr
            else:
                return f'Success employee has been set Inactive!'
        else:
            return validID
        
    """
    Assign a manager to a team
    """
    @staticmethod
    def assignManagerToTeam(managerId, teamId):
        validID = super().isfixed(managerId, "employeeID")
        validTeam = super().isfixed(teamId,"teamID")
        if validID == True and validTeam == True:
            setTeam=AdminPersistenceService.assignManagerToTeam(managerId, teamId)
            if setTeam.contains("mysql.connector.errors"): 
                return f'An error occurred assigning the manager to team due to an invalid value'
            else if setTeam[0] == 0 or setTeam[1] == 0 or setTeam[2] == 0 or setTeam[3] == 0:
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
        # create isFixed team and is MAx team
        if super().isfixed(team.teamId, "teamID") != True:
            return f'Invalid teamID. Input must be 4 characters'
            
        if team.managerId is not None:
            if super().isfixed(team.managerId, "employeeID") != True:
                return f'Invalid ManagerID. Input must be 6 characters'
        else:
            team.managerId = "NULL"
            
        if team.projectId is not None:
            if super().isfixedTP(team.projectId, "projectID") != True:
                return f'Invalid projectID. Input must be 8 characters'
        else:
            team.projectId = "NULL"
            
        if team.name is not None:
            if self.isMaxTP(team.name, "teamName") != True:
                return f'Invalid team name. Input must be max 20 characters'
        else:
            team.name = "NULL"
        
        if team.teamMembers != []:
            for member in team.teamMembers:
                if super().isfixed(member, "employeeID") != True:
                    retStr = "Invalid employeeID for team member: " + member + " , employeeID must be 8 characters"
                    return retStr
        
        makeTeam=AdminPersistenceService.createTeam(team)
        if makeTeam.contains("mysql.connector.errors"): 
            return f'An error occurred creating the team'
        else
            return f'Success team has been created!'

    """
    Create project with data stored in Project object
    """
    @staticmethod
    def createProject(project: Project):
        AdminPersistenceService.createProject(project)
        if self.isfixedTP(project.projectId, "projectID") != True:
            return f'Invalid projectID. Input must be 8 characters'
            
        if project.name is not None:
            if self.isMaxTP(project.name, "projectName") != True:
                return f'Invalid project name. Input must be max 20 characters'
        else:
            project.name = "NULL"
            
        if project.currentTeamId is not None:
            if super().isfixed(project.currentTeamId, "teamID") != True:
                return f'Invalid team name. Input must be 4 characters'
        else:
            team.name = "NULL"
            
        if project.status is not None:
            if self.isMaxTP(project.status, "projectStatus") != True:
                return f'Invalid team name. Input must be max 20 characters'
        else:
            team.name = "NULL"
        
        makeProject=AdminPersistenceService.createProject(project)
        if makeProject.contains("mysql.connector.errors"): 
            return f'An error occurred creating the project'
        else
            return f'Success project has been created!'