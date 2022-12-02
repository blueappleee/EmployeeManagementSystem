from Data_Objects.Employee import Employee
from Data_Objects.SysAdmin import SysAdmin
from Data_Objects.Team import Team
from Data_Objects.Project import Project
from db import dbConnection
import mysql.connector, sys


"""
Admin Persistence Service receives calls from Admin Controller and interacts with the database
"""
class AdminPersistenceService:
    def __init__(self):
        pass
        
    def addQuotes(attribute):
        if attribute is not None and attribute != "NULL":
            retstr = '"' + attribute + '"'
            
        else:
            retstr = 'NULL'
            
        return retstr

    """
    Search for admin by id to return
    """
    @staticmethod
    def searchAdminById(adminId) -> SysAdmin:
        cur = dbConnection.connection.cursor()

        try:
            query='SELECT * FROM employee WHERE employeeID=' + AdminPersistenceService.addQuotes(adminId) + ''
            cur.execute(query)
            result=cur.fetchall()
            sysAdmin = SysAdmin(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9],
                 result[10], result[11], result[12], result[13], result[14],
                 result[15], result[16], result[17], result[18], result[19], result[20])
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        #dbConnection.connection.close()
        
        return sysAdmin

    """
    Update Employee Role
    """
    @staticmethod
    def setEmployeeRole(employeeId, role):
        cur = dbConnection.connection.cursor()
        try:
            query='UPDATE employee SET empType=' + AdminPersistenceService.addQuotes(role) + ' WHERE employeeID=' + AdminPersistenceService.addQuotes(employeeId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            posResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
            
        return posResult

    """
    Register new Employee
    """
    @staticmethod
    def registerNewEmployee(employee: Employee):
        cur = dbConnection.connection.cursor()
        teamI=""
        manI=""
        #update usecase, this doesnt need to include setEmployeeRoel??
        try:
            query='INSERT INTO employee (employeeID, password, empType, teamID, managerID, fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES (' + AdminPersistenceService.addQuotes(employee.employeeId) + ', ' + AdminPersistenceService.addQuotes(employee.password) + ', ' + AdminPersistenceService.addQuotes(employee.empType) + ', ' + AdminPersistenceService.addQuotes(employee.teamId) + ', ' + AdminPersistenceService.addQuotes(employee.managerId) + ', ' + AdminPersistenceService.addQuotes(employee.fName) + ', ' + AdminPersistenceService.addQuotes(employee.lName) + ', ' + AdminPersistenceService.addQuotes(employee.salary) + ', ' + AdminPersistenceService.addQuotes(employee.position) + ', ' + AdminPersistenceService.addQuotes(employee.startDate) + ', ' + AdminPersistenceService.addQuotes(employee.birthDate) + ', ' + AdminPersistenceService.addQuotes(employee.sickDaysYearly) + ', ' + AdminPersistenceService.addQuotes(employee.sickDaysRemaining) + ', ' + AdminPersistenceService.addQuotes(employee.vacationDaysYearly) + ', ' + AdminPersistenceService.addQuotes(employee.vacationDaysRemaining) + ', ' + AdminPersistenceService.addQuotes(employee.address) + ', ' + AdminPersistenceService.addQuotes(employee.phoneNumber) + ', ' + AdminPersistenceService.addQuotes(employee.workEmail) + ', ' + AdminPersistenceService.addQuotes(employee.personalEmail) + ', ' + AdminPersistenceService.addQuotes(employee.directDepositNumber) + ', ' + AdminPersistenceService.addQuotes(employee.ssn) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            empI=cur.rowcount
        except mysql.connector.Error as error:
            # error if employeeId already taken or not null value isnt set
            print(error)
            return error
            
        if employee.teamId is not None:
            try:
                query='INSERT INTO teamMembers (teamID, employeeID) VALUES (' + AdminPersistenceService.addQuotes(employee.teamId) + ' , ' + AdminPersistenceService.addQuotes(employee.employeeId) + ')'
                cur.execute(query)
                dbConnection.connection.commit()
                teamI=cur.rowcount
            except mysql.connector.Error as error:
                # error if team doesnt exist
                print(error)
                return error
            
        if employee.managerId is not None:
            try:
                query='INSERT INTO empManaged (managerID, employeeID) VALUES (' + AdminPersistenceService.addQuotes(employee.managerId) + ' , ' + AdminPersistenceService.addQuotes(employee.employeeId) + ')'
                cur.execute(query)
                dbConnection.connection.commit()
                manI=cur.rowcount
            except mysql.connector.Error as error:
                # error if team doesnt exist
                print(error)
                return error
            
        #dbConnection.connection.close()
        return [empI, teamI, manI]

    """
    Make active employee inactive
    """
    @staticmethod 
    def setEmployeeInactive(employeeId):
        cur = dbConnection.connection.cursor()
        try:
            query='DELETE FROM empManaged WHERE employeeID=' + AdminPersistenceService.addQuotes(employeeId) + ''
            cur.execute(query)
            teamManRowExists = False
            managedResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
            
        try:
            query='DELETE FROM teamMembers WHERE employeeID=' + AdminPersistenceService.addQuotes(employeeId) + ''
            cur.execute(query)
            memberResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
    
        try:
            query='UPDATE employee SET position="Inactive" WHERE employeeID=' + AdminPersistenceService.addQuotes(employeeId) + ''
            cur.execute(query)
            posResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
            
        return [managedResult, memberResult, posResult]

    """
    Update Database to assign a manager to a team
    """
    @staticmethod
    def assignManagerToTeam(managerId, teamId):
        # will return error if team doesnt already exist
        cur = dbConnection.connection.cursor()

        try:
            query='UPDATE team SET teamManagerID=' + AdminPersistenceService.addQuotes(managerId) + ' WHERE teamID=' + AdminPersistenceService.addQuotes(teamId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            teamI= cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            return error
            
            
        try:
            query='UPDATE employee SET teamID=' + AdminPersistenceService.addQuotes(teamId) + ' WHERE employeeID=' + AdminPersistenceService.addQuotes(managerId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            empI= cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            return error
              
        try:
            query='SELECT * FROM teamMembers WHERE employeeID=' + AdminPersistenceService.addQuotes(managerId) + ''
            cur.execute(query)
            teamRowExists = False
            memberResult = cur.fetchall()
            teamMemI=""
            
            for row in memberResult:
                if row[0] != teamId:
                    dropQuery = 'DELETE FROM teamMembers WHERE employeeID=' + AdminPersistenceService.addQuotes(managerId) + ' AND teamID=' + AdminPersistenceService.addQuotes(teamId) + ''
                    cur.execute(dropQuery)
                    dbConnection.connection.commit()
                else:
                    teamRowExists=True
                    
            if teamRowExists==False:
                try:
                    query='INSERT INTO teamMembers (teamID, employeeID) VALUES (' + AdminPersistenceService.addQuotes(teamId) + ', ' + AdminPersistenceService.addQuotes(managerId) +  ')'
                    cur.execute(query)
                    dbConnection.connection.commit()
                    teamMemI = cur.rowcount
                except mysql.connector.Error as error:
                    print(error)
                    return error
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        
        try:
            query='SELECT * FROM teamManaged WHERE managerID=' + AdminPersistenceService.addQuotes(managerId) + ''
            cur.execute(query)
            teamManRowExists = False
            managedResult = cur.fetchall()
            teamManI=""
            
            for row in managedResult:
                if row[1] != teamId:
                    dropQuery = 'DELETE FROM teamManaged WHERE managerID=' + AdminPersistenceService.addQuotes(managerId) + ' AND teamID=' + AdminPersistenceService.addQuotes(teamId) + ''
                    cur.execute(dropQuery)
                    dbConnection.connection.commit()
                else:
                    teamManRowExists=True
                    
            if teamManRowExists==False:
                try:
                    query='INSERT INTO teamManaged (managerID, teamID) VALUES (' + AdminPersistenceService.addQuotes(managerId) + ', ' + AdminPersistenceService.addQuotes(teamId) +  ')'
                    cur.execute(query)
                    dbConnection.connection.commit()
                    teamManI = cur.rowcount
                except mysql.connector.Error as error:
                    print(error)
                    return error
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        
        
        #dbConnection.connection.close()
        return [teamI, empI, teamMemI, teamManI]

    """
    Create new record in Team table for team with data stored in Team object
    """
    @staticmethod
    def createTeam(team: Team):
        cur = dbConnection.connection.cursor()

        try:
            query='INSERT INTO team (teamID, teamManagerID, teamName, projectID) VALUES ('+ AdminPersistenceService.addQuotes(team.teamId) + ', ' + AdminPersistenceService.addQuotes(team.managerId) + ', ' + AdminPersistenceService.addQuotes(team.name) + ', ' + AdminPersistenceService.addQuotes(team.projectId) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            teamI = cur.rowcount
        except mysql.connector.Error as error:
            # potential errors: project needs to exist before adding team with an active project
            print(error)
            return error
            
        # fix this to insert into teamMembers table    
        membersI = []
        if team.teamMembers != []:
            for member in team.teamMembers:
                try:
                    query='INSERT INTO teamMember (teamID, employeeID) VALUES (' + AdminPersistenceService.addQuotes(team.teamId) + ', ' + AdminPersistenceService.addQuotes(member) + ')'
                    cur.execute(query)
                    dbConnection.connection.commit()
                    membersI.append(cur.rowcount)
                    
                    query='UPDATE employee SET teamID=' + AdminPersistenceService.addQuotes(team.teamId) + ' WHERE employeeID=' + AdminPersistenceService.addQuotes(member) + ''
                    cur.execute(query)
                    dbConnection.connection.commit()
                    membersI.append(cur.rowcount)
                except mysql.connector.Error as error:
                    print(error)
                    return error
        
        #dbConnection.connection.close()
        return [teamI, membersI]
        
    """
    Create new record in Project table for project with data stored in Project object
    """
    @staticmethod
    def createProject(project: Project):
        cur = dbConnection.connection.cursor()

        try:
            query='INSERT INTO project (projectID, projectName, currentTeamID, projectStatus) VALUES (' + AdminPersistenceService.addQuotes(project.projectId) + ', ' + AdminPersistenceService.addQuotes(project.name) + ', ' + AdminPersistenceService.addQuotes(project.currentTeamId) + ', ' + AdminPersistenceService.addQuotes(project.status) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            projrows= cur.rowcount
        except mysql.connector.Error as error:
            # potential errors: team does not exist
            print(error)
            return error
            
        
        try:
            query='UPDATE team SET projectID=' + AdminPersistenceService.addQuotes(project.projectId) + ' WHERE teamID=' + AdminPersistenceService.addQuotes(project.currentTeamId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            teamI= cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            return error
            
        #dbConnection.connection.close()
        return [projrows,teamI]
