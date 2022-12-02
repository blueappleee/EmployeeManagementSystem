from Data_Objects.Employee import Employee
from db import dbConnection
import mysql.connector

"""
Employee Persistence Service receives calls from Employee Controller and interacts with the database
"""
class EmployeePersistenceService:
    def __init__(self):
        pass
    
    """
    Add quotes if not null
    """
    @staticmethod
    def addQuotes(attribute):
        if attribute is not None and attribute != "NULL":
            retstr = '"' + str(attribute) + '"'
            
        else:
            retstr = 'NULL'
            
        return retstr
        
    """
    Search for employee by id return
    """
    @staticmethod
    def searchEmployeeById(employeeId) -> Employee:
        cur = dbConnection.connection.cursor()

        try:
            query='SELECT * FROM employee WHERE employeeID=' + EmployeePersistenceService.addQuotes(employeeId) + ''
            cur.execute(query)
            result=cur.fetchone()
            print(result)
            employee = Employee(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9],
                 result[10], result[11], result[12], result[13], result[14],
                 result[15], result[16], result[17], result[18], result[19], result[20])
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        #dbConnection.connection.close()
        
        return employee

    """
    Update Employee record in Employee Table
    """
    @staticmethod
    def updateEmployeeInformation(employee: Employee):
        cur = dbConnection.connection.cursor()
        empU = ""
        teamMemI=""
        managedI=""
        try:
            query='UPDATE employee SET password=' + EmployeePersistenceService.addQuotes(employee.password) + ', empType=' + EmployeePersistenceService.addQuotes(employee.empType) + ', teamID=' + EmployeePersistenceService.addQuotes(employee.teamId) + ', managerID=' + EmployeePersistenceService.addQuotes(employee.managerId) + ', fname=' + EmployeePersistenceService.addQuotes(employee.fName) + ', lname=' + EmployeePersistenceService.addQuotes(employee.lName) + ', salary=' + EmployeePersistenceService.addQuotes(employee.salary) + ', position=' + EmployeePersistenceService.addQuotes(employee.position)+ ', startDate=' + EmployeePersistenceService.addQuotes(employee.startDate) + ', birthDate=' + EmployeePersistenceService.addQuotes(employee.birthDate) + ', sickDaysYearly=' + EmployeePersistenceService.addQuotes(employee.sickDaysYearly) + ', sickDaysRemaining=' + EmployeePersistenceService.addQuotes(employee.sickDaysRemaining) + ', vacationDaysYearly=' + EmployeePersistenceService.addQuotes(employee.vacationDaysYearly) + ', vacationDaysRemaining=' + EmployeePersistenceService.addQuotes(employee.vacationDaysRemaining) + ', address=' + EmployeePersistenceService.addQuotes(employee.address) + ', phonenumber=' + EmployeePersistenceService.addQuotes(employee.phoneNumber) + ', workEmail=' + EmployeePersistenceService.addQuotes(employee.workEmail) + ', personalEmail=' + EmployeePersistenceService.addQuotes(employee.personalEmail) + ', directDepositNumber=' + EmployeePersistenceService.addQuotes(employee.directDepositNumber) + ', ssn=' + EmployeePersistenceService.addQuotes(employee.ssn) + ' WHERE employeeID=' + EmployeePersistenceService.addQuotes(employee.employeeId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            empU=cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
          
        if employee.teamId is not None:
            try:
                query='SELECT * FROM teamMembers WHERE employeeID=' + EmployeePersistenceService.addQuotes(employee.employeeId) + ''
                cur.execute(query)
                teamRowExists = False
                memberResult = cur.fetchall()
                
                for row in memberResult:
                    if row[0] != teamId:
                        dropQuery = 'DELETE FROM teamMembers WHERE employeeID=' + EmployeePersistenceService.addQuotes(employee.employeeId) + ' AND teamID=' + EmployeePersistenceService.addQuotes(employee.teamId) + ''
                        cur.execute(sql)
                        dbConnection.connection.commit()
                    else:
                        teamRowExists=True
                        
                if teamRowExists==False:
                    try:
                        query='INSERT INTO teamMembers (teamID, employeeID) VALUES (' + EmployeePersistenceService.addQuotes(employee.teamId) + ', ' + EmployeePersistenceService.addQuotes(employee.employeeId) +  ')'
                        cur.execute(query)
                        dbConnection.connection.commit()
                        teamMemI = cur.rowcount
                    except mysql.connector.Error as error:
                        print(error)
                        return error
                
            except mysql.connector.Error as error:
                print(error)
                return error
            
        if employee.managerId is not None:
            try:
                query='SELECT * FROM empManaged WHERE employeeID=' + EmployeePersistenceService.addQuotes(employee.employeeId) + ''
                cur.execute(query)
                teamRowExists = False
                managedResult = cur.fetchall()
                
                for row in managedResult:
                    if row[0] != employee.managerId:
                        dropQuery = 'Delete FROM empManaged WHERE employeeID=' + EmployeePersistenceService.addQuotes(employee.employeeId) + ' AND managerID=' + EmployeePersistenceService.addQuotes(employee.managerId) + ''
                        cur.execute(sql)
                        dbConnection.connection.commit()
                    else:
                        teamRowExists=True
                        
                if teamRowExists==False:
                    try:
                        query='INSERT INTO empManaged (managerID, employeeID) VALUES (' + EmployeePersistenceService.addQuotes(employee.managerId) + ' , ' + EmployeePersistenceService.addQuotes(employee.employeeId) + ')'
                        cur.execute(query)
                        dbConnection.connection.commit()
                        managedI=cur.rowcount
                    except mysql.connector.Error as error:
                        print(error)
                        return error
                
            except mysql.connector.Error as error:
                print(error)
                return error    
                
        #dbConnection.connection.close()
        return (empU,teamMemI,managedI)

    """
    Update Employee's work hours
    """
    @staticmethod
    def logWorkHours(employee: Employee, workType, workTime, workDate):
        cur = dbConnection.connection.cursor()
        teamHourI=""
	
        try:
            query='INSERT INTO hoursWorked (employeeID, hourType, hourAmount, workDate) VALUES (' + EmployeePersistenceService.addQuotes(employee.employeeId) + ', ' + EmployeePersistenceService.addQuotes(workType) + ', ' + EmployeePersistenceService.addQuotes(workTime) + ', ' + EmployeePersistenceService.addQuotes(workDate) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            hoursWorkedR = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            return error
            
        if employee.teamId is not None:
            try:
                query='SELECT projectID FROM team WHERE teamID=' + EmployeePersistenceService.addQuotes(employee.teamId) + ''
                cur.execute(query)
                projectIDR=cur.fetchall()
                projectID=projectIDR[0][0]

            except mysql.connector.Error as error:
                print(error)
                sys.exit(1)
        
            try:
                query='SELECT * FROM teamHoursWorked WHERE teamID=' + EmployeePersistenceService.addQuotes(employee.teamId) + ' AND projectID=' + EmployeePersistenceService.addQuotes(projectID) + ''
                cur.execute(query)
                teamRowExists = False
                teamHoursResult = cur.fetchall()

                if teamHoursResult == []:
                    try:
                        query='INSERT INTO teamHoursWorked (teamID, projectID, hourAmount) VALUES (' + EmployeePersistenceService.addQuotes(employee.teamId) + ', ' + EmployeePersistenceService.addQuotes(projectID) + ', ' + EmployeePersistenceService.addQuotes(workTime) + ')'
                        cur.execute(query)
                        dbConnection.connection.commit()
                        teamHourI = cur.rowcount
                    except mysql.connector.Error as error:
                        print(error)
                        return error
                else:
                    newHours = int(teamHoursResult[0][2]) + int(workTime)
                    try:
                        query='UPDATE teamHoursWorked set hourAmount=' + EmployeePersistenceService.addQuotes(newHours) + ' WHERE teamID=' + EmployeePersistenceService.addQuotes(employee.teamId) + ' AND projectID=' + EmployeePersistenceService.addQuotes(projectID) +  ''
                        cur.execute(query)
                        dbConnection.connection.commit()
                        teamHourI = cur.rowcount
                    except mysql.connector.Error as error:
                        print(error)
                        return error
                        
            except mysql.connector.Error as error:
                print(error)
                sys.exit(1)  
            
        #dbConnection.connection.close()
        return (hoursWorkedR, teamHourI)
