import datetime

from Data_Objects.Manager import Manager
from Data_Objects.Manager import Employee
from Data_Objects.Project import Project
from Data_Objects.HoursWorked import TeamHoursWorked
from Persistence.ManagerPersistenceService import ManagerPersistenceService
from Business_Logic.EmployeeController import EmployeeController
from tabulate import tabulate


def validateDate(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
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
            if EmployeeController.istime(workHours, 'work hours'):
                result=ManagerPersistenceService.correctTeamEmployeeWorkHours(teamEmployeeId, hourType, workHours, workDate)
                if result==0:
                    return None
                elif result==1:
                    return f'An error occurred assigning the employee to the team'
                else:
                    return f'Work Entry not found'
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
                retstr ="The team contains employees: "
                for i in range(len(employeeList)):
                    emp=employeeList[i]
                    retstr=retstr+emp.employeeId + " Name: " + emp.fName + " " + emp.lName + " in position: " + emp.position
                    if  i != len(employeeList) - 1:
                        retstr=retstr+" and also "
                return retstr
        else:
            return f'The input teamId does not match the length requirement.'

    """
    Get Specific Team Employee's work related data
    """
    @staticmethod
    def getTeamEmployeeWorkData(teamID, teamEmployeeID):
        if len(teamID) == 4:
            hourList = ManagerPersistenceService.getTeamEmployeeWorkData(teamID, teamEmployeeID)
            if hourList is None or (type(hourList) == "List" and len(hourList) == 0):
                return f'The employee does not have any work yet.'
            elif type(hourList) != "List" and hourList == 1:
                return f'An error occurred getting the employee.'
            else:
                retstr ="The employee has worked: "
                for i in range(len(hourList)):
                    hour=hourList[i]
                    retstr=retstr+ str(hour.hourAmount) + "hours on Date: " + str(hour.workDate) + " of type " + str(hour.hourType) + " " 
                    if  i != len(hourList) - 1:
                        retstr=retstr+" and also "
                return retstr
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
                    result= ManagerPersistenceService.assignEmployeeToTeam(teamEmployeeId, managerId, teamID)
                    if result==0:
                    	return None
                    else:
                        return f'An error occurred assigning the employee to the team'
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
                result=ManagerPersistenceService.removeEmployeeFromTeam(teamID, teamEmployeeId)
                if result==111:
                    return f'An error occurred removing the employee'
                elif result==0:
                    return f"The employee isn't in that team"
                else:
                    return None
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
                result = ManagerPersistenceService.assignTeamProject(projectId, teamId)
                if result==0:
                    return None
                else:
                    return f'An error occurred assigning the employee to the team'
            else:
                return f'The input teamID does not match length requirement.'
        else:
            return f'The input projectID does not match length requirement.'

    """
    Get project details
    """
    @staticmethod
    def getProjectDetails(projectId) -> Project:
        if len(projectId) == 8:
            projectInstance = ManagerPersistenceService.getProjectDetails(projectId)
            if projectInstance is None:
                return f'The project does not exist in our system.'
            else:
                return projectInstance
        else:
            return f'The input projectID does not match length requirement.'
