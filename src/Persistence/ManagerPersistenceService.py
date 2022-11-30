from src import dbConnection
from src.Data_Objects.Project import Project
from src.Data_Objects.Employee import Employee
from src.Data_Objects.Manager import Manager
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
    def correctTeamEmployeeWorkHours(teamEmployeeId, workHours, workDate):
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("UPDATE hoursWorked SET hourAmount = '%(1)s', workDate = '%(2)s' WHERE employeeID = '%(3)s';" % {"1": workHours, "2": workDate, "3": teamEmployeeId})

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

        print("The system has updated the correct working hours for employee (" + teamEmployeeId + ").")

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
                employeeInfo = cur.fetchall()

                employeeInstance = Employee(employeeInfo[0], employeeInfo[1], employeeInfo[2], employeeInfo[3], employeeInfo[4], employeeInfo[5],
                                            employeeInfo[6], employeeInfo[7], employeeInfo[8], employeeInfo[9], employeeInfo[10], employeeInfo[11],
                                            employeeInfo[12], employeeInfo[13], employeeInfo[14], employeeInfo[15], employeeInfo[16], employeeInfo[17],
                                            employeeInfo[18], employeeInfo[19], employeeInfo[20])

                employeeList.append(employeeInstance)

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

        return employeeList

    """
    Get Specific Team Employee's work related data
    """
    @staticmethod
    def getTeamEmployeeWorkData(teamID, teamEmployeeID):
        cur = dbConnection.connection.cursor()

        try:
            # FIXME wait for testing the sql query
            cur.execute("SELECT project.projectID, project.projectName, project.currentTeamID, project.projectStatus FROM project, team, employee WHERE team.teamID = project.currentTeamID AND team.teamID = employee.teamID AND employee.employeeID = '%(1)s' AND employee.teamID = '%(2)s';" % {"1": teamEmployeeID, "2": teamID})

            records = cur.fetchall()
            projectList = []
            for row in records:
                projectInstance = Project(row[0], row[1], row[2], row[3])
                # projectInstance.projectId = row[0]
                # projectInstance.Name = row[1]
                # projectInstance.currentTeamId = row[2]
                # projectInstance.status = row[3]

                projectList.append(projectInstance)

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

        return projectList

    """
    Assign Employee to team
    """
    @staticmethod
    def assignEmployeeToTeam(teamEmployeeId, managerId, teamID):
        cur = dbConnection.connection.cursor()

        try:
            # update the team information to the employee table
            cur.execute("UPDATE employee SET teamID = '%(1)s' WHERE employeeID = '%(2)s';" % {"1": teamID, "2": teamEmployeeId})

            # insert the employee information to the teamMembers table
            cur.execute("INSERT INTO teamMembers VALUES ('%(1)s', '%(2)s');" % {"1": teamID, "2": teamEmployeeId})

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

        print("The employee (" + teamEmployeeId + ") has been added to the team (" + teamID + "), which managed by the Manager (" + managerId + ").")

    """
    Remove Employee from team
    """
    @staticmethod
    def removeEmployeeFromTeam(teamID, teamEmployeeId):
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("DELETE FROM teamMembers WHERE teamID = '%(1)s' AND employeeID = '%(2)s';" % {"1": teamID, "2": teamEmployeeId})

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

        print("The employee (" + teamEmployeeId + ") has been successfully removed from the team (" + teamID + ").")

    """
    Assign Team to Project
    """
    @staticmethod
    def assignTeamProject(projectId, teamId):
        cur = dbConnection.connection.cursor()

        try:
            # update the project information to the Team table
            cur.execute("UPDATE team SET projectID = '%(1)s' WHERE teamID = '%(2)s';" % {"1": projectId, "2": teamId})

            # update the team information to the project table
            cur.execute("UPDATE project SET currentTeamID = '%(1)s' WHERE projectID = '%(2)s';" % {"1": teamId, "2": projectId})

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

        print("The team has been successfully assigned to a project.")

    """
    Get project details
    """
    @staticmethod
    def getProjectDetails(projectID):
        cur = dbConnection.connection.cursor()

        try:
            cur.execute("SELECT * FROM project WHERE projectID = '%(1)s';" % {"1": projectID})
            record = cur.fetchall()
            print("Total number of rows in table", cur.rowcount)

            projectInstance = Project(record[0], record[1], record[2], record[3])

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

        return projectInstance

    """
        search the manager by id
        """
    @staticmethod
    def searchManagerByID(managerID) -> Manager:
        cur = dbConnection.connection.cursor()

        try:
            # cur.execute("SELECT employeeId, empType, teamId, managerId, fName, lName, salary, position, phoneNumber, workEmail FROM employee WHERE employeeID = '%(1)s' AND empType = mng;" % {"1": managerID})
            cur.execute("SELECT * FROM employee WHERE employeeID = '%(1)s' AND empType = mng;" % {"1": managerID})
            record = cur.fetchall()
            # print("Total number of rows in table", cur.rowcount)

            managerInstance = Manager(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                      record[7], record[8], record[9], record[10], record[11], record[12], record[13],
                                      record[14], record[15], record[16], record[17], record[18], record[19], record[20])

        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()

        return managerInstance
