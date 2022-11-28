from Data_Objects.Manager import Manager
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
    Search for employee by id return
    """
    @staticmethod
    def searchManagerById(managerId) -> Manager:
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
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("SELECT * FROM team WHERE teamID = '%(1)s';" % {"1" : teamId})
        # FIXME store the query results into data objects

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

    """
    Get Specific Team Employee's work related data
    """
    @staticmethod
    def getTeamEmployeeWorkData(teamEmployeeId):
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("SELECT fname, lname, projectName FROM project, team, employee WHERE employee.employeeID = teamEmployeeID AND ")
            # FIXME store the query results into data objects

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

    """
    Assign Employee to team
    """
    @staticmethod
    def assignEmployeeToTeam(teamEmployeeId, managerId):
        cur = dbConnection.connection.cursor()

        try:
            # FIXME wrong query so far, will fix it later
            cur.execute("INSERT INTO team () '%(1)s';" % {"1": managerId})
            # FIXME store the query results into data objects

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

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
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("SELECT * FROM project WHERE projectID = '%(1)s';" % {"1": projectID})
        # FIXME store the query results into data objects

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()