from src import dbConnection
import sys
import mysql.connector
from mysql.connector import Error


"""
Manager Persistence Service receives calls from Manager Controller and interacts with the database
"""
class ManagerPersistenceService:
    def __init__(self):
        pass

    """
    Logic to correct a team employee's work hours
    """
    @staticmethod
    def correctTeamEmployeeWorkHours(teamEmployeeId, workHours):
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("UPDATE hoursWorked SET hourAmount = " + workHours + "WHERE employeeID = " + teamEmployeeId)
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

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
    def getProjectDetails():
        pass
