import datetime

from Data_Objects.Manager import Manager
from Persistence import ManagerPersistenceService
from tabulate import tabulate


def validateDate(date):
    try:
        datetime.datetime.striptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


"""
Manager Controller that Manager Interface will call for logic of process
"""
class ManagerController:
    def __init__(self):
        pass

    """
    Get Manager by Id
    """
    @staticmethod
    def getManagerById(managerId):
        # managerInstance = Manager()
        if len(managerId) == 6:
            managerInstance = ManagerPersistenceService.searchManagerByID(managerId)
            if managerInstance is None:
                return f'There is no such Manager in our system.'
            else:
                return managerInstance
                # headers = ["employeeId", "empType", "teamId", "managerId", "fName", "lName", "salary", "position", "phoneNumber", "workEmail"]
                # print(tabulate(managerInstance, headers, tablefmt="grid"))
        else:
            return f'The input managerId does not match the length requirement.'

    """
    Logic to correct a team employee's work hours
    """
    @staticmethod
    def correctTeamEmployeeWorkHours(teamEmployeeId, hourType, workHours, workDate):
        if len(teamEmployeeId) == 6:
            if isinstance(workHours, int):
                if validateDate(workDate):
                    ManagerPersistenceService.correctTeamEmployeeWorkHours(teamEmployeeId, hourType, workHours, workDate)
            else:
                return f'The input work hours is not an integer.'
        else:
            return f'The input employeeID does not match the length requirement.'

    """
    Get summary stats on team's employees
    """
    @staticmethod
    def getSummaryTeamEmployeeData(teamId):
        if len(teamId) == 4:
            employeeList = ManagerPersistenceService.getSummaryTeamEmployeeData(teamId)
            if employeeList is None or len(employeeList) == 0:
                return f'There is no employee in such team currently.'
            else:
                return employeeList
        else:
            return f'The input teamId does not match the length requirement.'

    """
    Get Specific Team Employee's work related data
    """
    @staticmethod
    def getTeamEmployeeWorkData(teamID, teamEmployeeID):
        if len(teamID) == 4:
            projectList = ManagerPersistenceService.getTeamEmployeeWorkData(teamID, teamEmployeeID)
            if projectList is None or len(projectList) == 0:
                return f'The employee does not have any project yet.'
            else:
                return projectList
        else:
            return f'The input teamId does not match the length requirement.'

    """
    Assign Employee to team
    """
    @staticmethod
    def assignEmployeeToTeam(teamEmployeeId, managerId, teamID):
        if len(teamEmployeeId) == 6:
            if len(managerId) == 6:
                if len(teamID) == 4:
                    ManagerPersistenceService.assignEmployeeToTeam(teamEmployeeId, managerId, teamID)
                else:
                    return f'The input teamID does not match length requirement.'
            else:
                return f'The input managerID does not match length requirement.'
        else:
            return f'The input employeeID does not match length requirement.'

    """
    Remove Employee from team
    """
    @staticmethod
    def removeEmployeeFromTeam(teamID, teamEmployeeId):
        if len(teamID) == 4:
            if len(teamEmployeeId) == 6:
                ManagerPersistenceService.removeEmployeeFromTeam(teamID, teamEmployeeId)
            else:
                return f'The input employeeID does not match length requirement.'
        else:
            return f'The input teamID does not match length requirement.'

    """
    Assign Team to Project
    """
    @staticmethod
    def assignTeamProject(projectId, teamId):
        if len(projectId) == 8:
            if len(teamId) == 4:
                ManagerPersistenceService.assignTeamProject(projectId, teamId)
            else:
                return f'The input teamID does not match length requirement.'
        else:
            return f'The input projectID does not match length requirement.'

    """
    Get project details
    """
    @staticmethod
    def getProjectDetails(projectId):
        if len(projectId) == 8:
            projectInstance = ManagerPersistenceService.getProjectDetails(projectId)
            if projectInstance is None:
                return f'The project does not exist in our system.'
            else:
                return projectInstance
        else:
            return f'The input projectID does not match length requirement.'
