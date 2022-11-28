from Data_Objects.Employee import Employee
from Data_Objects.SysAdmin import SysAdmin
from Data_Objects.Team import Team
from Data_Objects.Project import Project

"""
Admin Persistence Service receives calls from Admin Controller and interacts with the database
"""
class AdminPersistenceService:
    def __init__(self):
        pass

    """
    Search for admin by id to return
    """
    @staticmethod
    def searchAdminById(adminId) -> SysAdmin:
        pass

    """
    Update Employee Role
    """
    @staticmethod
    def setEmployeeRole(employeeId, role):
        pass

    """
    Register new Employee
    """
    @staticmethod
    def registerNewEmployee(employee: Employee):
        pass

    """
    Make active employee inactive
    """
    @staticmethod
    def setEmployeeInactive(employeeId):
        pass

    """
    Update Database to assign a manager to a team
    """
    @staticmethod
    def assignManagerToTeam(managerId, teamId):
        pass

    """
    Create new record in Team table for team with data stored in Team object
    """
    @staticmethod
    def createTeam(team: Team):
        pass

    """
    Create new record in Project table for project with data stored in Project object
    """
    @staticmethod
    def createProject(project: Project):
        pass