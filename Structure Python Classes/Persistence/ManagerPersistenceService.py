from Data_Objects.Manager import Manager
"""
Manager Persistence Service receives calls from Manager Controller and interacts with the database
"""
class ManagerPersistenceService:
    def __init__(self):
        pass

    """
    Search for employee by id return
    """
    @staticmethod
    def searchManagerById(managerId) -> Manager:
        pass

    """
    Logic to correct a team employee's work hours
    """
    @staticmethod
    def correctTeamEmployeeWorkHours(teamEmployeeId):
        pass

    """
    Get summary stats on team's employees
    """
    @staticmethod
    def getSummaryTeamEmployeeData(teamId):
        pass

    """
    Get Specific Team Employee's work related data
    """
    @staticmethod
    def getTeamEmployeeWorkData(teamEmployeeId):
        pass

    """
    Assign Employee to team
    """
    @staticmethod
    def assignEmployeeToTeam(teamEmployeeId, managerId):
        pass

    """
    Remove Employee from team
    """
    @staticmethod
    def removeEmployeeFromTeam(teamEmployeeId):
        pass

    """
    Assign Team to Project
    """
    @staticmethod
    def assignTeamProject(projectId, teamId):
        pass

    """
    Get project details
    """
    @staticmethod
    def getProjectDetails(projectId):
        pass