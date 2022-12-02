from db import dbConnection
from Data_Objects.Project import Project
from Data_Objects.HoursWorked import TeamHoursWorked
from Data_Objects.Employee import Employee
from Data_Objects.Manager import Manager
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
    def correctTeamEmployeeWorkHours(teamEmployeeId, hourType, workHours, workDate):
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("UPDATE hoursWorked SET hourAmount = '%(1)s' WHERE  workDate = '%(2)s' AND hourType = '%(3)s' AND employeeID = '%(4)s';" % {"1": workHours, "2": workDate, "3": hourType, "4": teamEmployeeId})
            dbConnection.connection.commit()
            posResult = cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            return error
            
        if posResult==0:
            return 2
        else:
            return 0

    """
    Get summary stats on team's employees
    """
    @staticmethod
    def getSummaryTeamEmployeeData(teamID):
        cur = dbConnection.connection.cursor()

        try:
            # list all the employee information in this given team
            cur.execute("SELECT * FROM teamMembers WHERE teamID = '%(1)s';" % {"1": teamID})

            records = cur.fetchall()
            employeeList = []
            for row in records:
                employeeID = row[1]
                cur.execute("SELECT * FROM employee WHERE employeeID = '%(1)s';" % {"1": employeeID})
                employeeInfo = cur.fetchall()[0]

                employeeInstance = Employee(employeeInfo[0], employeeInfo[1], employeeInfo[2], employeeInfo[3], employeeInfo[4], employeeInfo[5],
                                            employeeInfo[6], employeeInfo[7], employeeInfo[8], employeeInfo[9], employeeInfo[10], employeeInfo[11],
                                            employeeInfo[12], employeeInfo[13], employeeInfo[14], employeeInfo[15], employeeInfo[16], employeeInfo[17],
                                            employeeInfo[18], employeeInfo[19], employeeInfo[20])

                employeeList.append(employeeInstance)

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)

        return employeeList

    """
    Get Specific Team Employee's work related data
    """
    @staticmethod
    def getTeamEmployeeWorkData(teamID, teamEmployeeID):
        cur = dbConnection.connection.cursor()

        try:
            # TODO wait for testing the sql query
            cur.execute("SELECT * FROM hoursWorked WHERE employeeID= '%(1)s';" % {"1": teamEmployeeID})

            records = cur.fetchall()
            workList = []
            for row in records:
                workInstance = TeamHoursWorked(row[0], row[1], row[2], row[3])

                workList.append(workInstance)

        except mysql.connector.Error as error:
            print(error)
            return 1

        return workList

    """
    Assign Employee to team
    """
    @staticmethod
    def assignEmployeeToTeam(teamEmployeeId, managerId, teamID):
        cur = dbConnection.connection.cursor()

        try:
            # remove the employee from current team
            cur.execute("DELETE FROM teamMembers WHERE employeeID = '%(1)s';" % {"1": teamEmployeeId})
            dbConnection.connection.commit()

            # update the team information to the employee table
            cur.execute("UPDATE employee SET teamID = '%(1)s' WHERE employeeID = '%(2)s';" % {"1": teamID, "2": teamEmployeeId})
            dbConnection.connection.commit()

            # insert the employee information to the teamMembers table
            cur.execute("INSERT INTO teamMembers VALUES ('%(1)s', '%(2)s');" % {"1": teamID, "2": teamEmployeeId})
            dbConnection.connection.commit()
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)

        return 0

    """
    Remove Employee from team
    """
    @staticmethod
    def removeEmployeeFromTeam(teamID, teamEmployeeId):
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("DELETE FROM teamMembers WHERE teamID = '%(1)s' AND employeeID = '%(2)s';" % {"1": teamID, "2": teamEmployeeId})
            dbConnection.connection.commit()
            result=cur.rowcount
            cur.execute("UPDATE employee SET teamID = NULL WHERE employeeID = '%(1)s';" % {"1": teamEmployeeId})
            dbConnection.connection.commit()

        except mysql.connector.Error as error:
            print(error)
            return 111

        return result

    """
    Assign Team to Project
    """
    @staticmethod
    def assignTeamProject(projectId, teamId):
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("UPDATE project SET currentTeamID=NULL WHERE currentTeamID = '%(2)s';" % {"1": teamId})
            dbConnection.connection.commit()
        
            # update the project information to the Team table
            cur.execute("UPDATE team SET projectID = '%(1)s' WHERE teamID = '%(2)s';" % {"1": projectId, "2": teamId})
            dbConnection.connection.commit()

            # update the team information to the project table
            cur.execute("UPDATE project SET currentTeamID = '%(1)s' WHERE projectID = '%(2)s';" % {"1": teamId, "2": projectId})
            dbConnection.connection.commit()

        except mysql.connector.Error as error:
            print(error)
            return error

        return 0

    """
    Get project details
    """
    @staticmethod
    def getProjectDetails(projectID):
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("SELECT * FROM project WHERE projectID = '%(1)s';" % {"1": projectID})
            record = cur.fetchone()
            #print("Total number of rows in table", cur.rowcount)

            projectInstance = Project(record[0], record[1], record[2], record[3])

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)

        return projectInstance

    """
    Search the manager by id
    """
    @staticmethod
    def searchManagerByID(managerID) -> Manager:
        cur = dbConnection.connection.cursor()

        try:
            # cur.execute("SELECT employeeId, empType, teamId, managerId, fName, lName, salary, position, phoneNumber, workEmail FROM employee WHERE employeeID = '%(1)s' AND empType = mng;" % {"1": managerID})
            cur.execute("SELECT * FROM employee WHERE employeeID = '%(1)s';" % {"1": managerID})
            record = cur.fetchone()
            # print("Total number of rows in table", cur.rowcount)

            managerInstance = Manager(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8], record[9], record[10], record[11], record[12], record[13],
                                      record[14], record[15], record[16], record[17], record[18], record[19], record[20])

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)

        return managerInstance
