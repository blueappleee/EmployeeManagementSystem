from Manager import Manager
from ManagerPersistenceService import ManagerPersistenceService

"""
Manager Controller that Manager Interface will call for logic of process
"""
class ManagerController:
    def __init__(self):
        pass

    """
    Logic to correct a team employee's work hours
    """
    @staticmethod
    def correctTeamEmployeeWorkHours(teamEmployeeId):
        ManagerPersistenceService.correctTeamEmployeeWorkHours(teamEmployeeId)
        pass

    """
    Get summary stats on team's employees
    """
    @staticmethod
    def getSummaryTeamEmployeeData(teamId):
        ManagerPersistenceService.getSummaryTeamEmployeeData(teamId)
        pass

    """
    Get Specific Team Employee's work related data
    """
    @staticmethod
    def getTeamEmployeeWorkData(teamEmployeeId):
        ManagerPersistenceService.getTeamEmployeeWorkData(teamEmployeeId)
        pass

    """
    Assign Employee to team
    """
    @staticmethod
    def assignEmployeeToTeam(teamEmployeeId, managerId):
        ManagerPersistenceService.assignEmployeeToTeam(teamEmployeeId, managerId)
        pass

    """
    Remove Employee from team
    """
    @staticmethod
    def removeEmployeeFromTeam(teamEmployeeId):
        ManagerPersistenceService.removeEmployeeFromTeam(teamEmployeeId)
        pass

    """
    Assign Team to Project
    """
    @staticmethod
    def assignTeamProject(projectId, teamId):
        ManagerPersistenceService.assignTeamProject(projectId, teamId)
        pass

    """
    Get project details
    """
    @staticmethod
    def getProjectDetails(projectId):
        ManagerPersistenceService.getProjectDetails(projectId)
        pass