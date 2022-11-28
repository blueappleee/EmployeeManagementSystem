from Data_Objects.Employee import Employee
from Data_Objects.SysAdmin import SysAdmin
from Data_Objects.Team import Team
from Data_Objects.Project import Project
from Persistence.AdminPersistenceService import AdminPersistenceService

"""
Admin Controller that Admin Interface will call for logic of process
"""
class AdminController:
    def __init__(self):
        pass

    """
    Search for admin by id to return
    """
    @staticmethod
    def searchAdminById(adminId) -> SysAdmin:
        return AdminPersistenceService.searchAdminById(adminId)
        pass

    """
    Set Employee Role
    """
    @staticmethod
    def setEmployeeRole(employeeId, role):
        AdminPersistenceService.setEmployeeRole(employeeId, role)
        pass

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
        AdminPersistenceService.setEmployeeInactive(employeeId)
        pass

    """
    Assign a manager to a team
    """
    @staticmethod
    def assignManagerToTeam(managerId, teamId):
        AdminPersistenceService.assignManagerToTeam(managerId, teamId)
        pass

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