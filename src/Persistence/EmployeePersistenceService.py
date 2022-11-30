from Data_Objects.Employee import Employee
"""
Employee Persistence Service receives calls from Employee Controller and interacts with the database
"""
class EmployeePersistenceService:
    def __init__(self):
        pass

    """
    Search for employee by id return
    """
    @staticmethod
    def searchEmployeeById(employeeId) -> Employee:
        cur = dbConnection.connection.cursor()

        try:
            query='SELECT * FROM employee WHERE employeeID="' employeeId + '"'
            cur.execute(query)
            result=cur.fetchall()
            employee = Employee(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9],
                 result[10], result[11], result[12], result[13], result[14],
                 result[15], result[16], result[17], result[18], result[19], result[20])
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()
        
        return employee

    """
    Update Employee record in Employee Table
    """
    @staticmethod
    def updateEmployeeInformation(employee: Employee):
        cur = dbConnection.connection.cursor()
        empU = ""
        teamMemI=""
        try:
            query='UPDATE employee SET password="' + employee.password
            + '", empType="' + employee.empType
            + '", teamID="' + employee.teamId
            + '", managerID="' + employee.managerId
            + '", fname="' + employee.fname 
            + '", lname="' + employee.lname
            + '", salary="' + employee.salary
            + '", position="' + employee.position
            + '", startDate="' + employee.startDate
            + '", birthDate="' + employee.birthDate
            + '", sickDaysYearly="' + employee.sickDaysYearly
            + '", sickDaysRemaining="' + employee.sickDaysRemaining
            + '", vacationDaysYearly="' employee.vacationDaysYearly
            + '", vacationDaysRemaining="' employee.vacationDaysRemaining
            + '", address="' + employee.address
            + '", phonenumber="' + employee.phonenumber
            + '", workEmail="' + employee.workEmail
            + '", personalEmail="' employee.personalEmail
            + '", directDepositNumber="' + employee.directDepositNumber
            + '", ssn="' + employee.ssn + '" WHERE employeeID="' + employee.employeeId + '"'
            cur.execute(query)
            dbConnection.connection.commit()
            empU=cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
          
        if employee.teamId != null:
            try:
                query='SELECT * FROM teamMembers WHERE employeeID="' employee.employeeId + '"'
                cur.execute(query)
                teamRowExists = False
                memberResult = cur.fetchall()
                teamMemI=""
                
                for row in memberResult:
                    if row[0] != teamId:
                        dropQuery = 'DELETE FROM teamMembers WHERE employeeID="' + employee.employeeId + '" AND teamID="' + employee.teamId + '"'
                        cur.execute(sql)
                        dbConnection.connection.commit()
                    else:
                        teamRowExists=True
                        
                if teamRowExists==False:
                    try:
                        query='INSERT INTO teamMembers (teamID, employeeID) VALUES ("' + employee.teamId + '", "' + employee.employeeId +  '")'
                        cur.execute(query)
                        dbConnection.connection.commit()
                        teamMemI = cur.rowcount
                    except mysql.connector.Error as error:
                        print(error)
                        return error
                
            except mysql.connector.Error as error:
                print(error)
                return error
            
        if employee.managerId != null:
            try:
                query='SELECT * FROM empManaged WHERE employeeID="' employee.employeeId + '"'
                cur.execute(query)
                teamRowExists = False
                managedResult = cur.fetchall()
                managedI=""
                
                for row in managedResult:
                    if row[0] != employee.managerId:
                        dropQuery = 'Delete FROM empManaged WHERE employeeID="' + employee.employeeId + '" AND managerID="' + employee.managerId + '"'
                        cur.execute(sql)
                        dbConnection.connection.commit()
                    else:
                        teamRowExists=True
                        
                if teamRowExists==False:
                    try:
                        query='INSERT INTO empManaged (managerID, employeeID) VALUES ("' + employee.managerId + '" , "' employee.employeeId + '")'
                        cur.execute(query)
                        dbConnection.connection.commit()
                        managedI=cur.rowcount
                    except mysql.connector.Error as error:
                        print(error)
                        return error
                
            except mysql.connector.Error as error:
                print(error)
                return error    
                
        dbConnection.connection.close()
        return (empU,teamMemI,managedI)

    """
    Update Employee's work hours
    """
    @staticmethod
    def logWorkHours(employee: Employee, workType, workTime, workDate):
        cur = dbConnection.connection.cursor()

        try:
            query='INSERT INTO hoursWorked ("employeeID", "hourType", "hourAmount", "workDate") VALUES ("' + Employee.employeeID + '", "' + workType + '", "' + workTime + '", "' + workDate + '")'
            cur.execute(query)
            mydb.commit()
            hoursWorkedR = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            return error
            
        if employee.teamId != null:
            try:
                query='SELECT projectID FROM team WHERE teamID="' employee.teamId + '"'
                cur.execute(query)
                projectIDR=cur.fetchall()
                projectID=projectIDR[0]

            except mysql.connector.Error as error:
                print(error)
                sys.exit(1)
        
            try:
                query='SELECT * FROM teamHoursWorked WHERE teamID="' employee.teamId + '" AND projectID="' + projectID + '"'
                cur.execute(query)
                teamRowExists = False
                teamHoursResult = cur.fetchall()
                teamHourI=""
                
                if teamHoursResult = []:
                    try:
                        query='INSERT INTO teamHoursWorked (teamID, projectID, hourAmount) VALUES ("' + employee.teamId + '", "' + projectID + '", "' + workTime + '")'
                        cur.execute(query)
                        dbConnection.connection.commit()
                        teamHourI = cur.rowcount
                    except mysql.connector.Error as error:
                        print(error)
                        return error
                else:
                    newHours = int(teamHoursResult[2]) + int(hourAmount)
                    try:
                        query='UPDATE teamHoursWorked set hourAmount="' + newHours + '" WHERE teamID="' + employee.teamId + '" AND projectID="' + projectID +  '"'
                        cur.execute(query)
                        dbConnection.connection.commit()
                        teamHourI = cur.rowcount
                    except mysql.connector.Error as error:
                        print(error)
                        return error
                        
            except mysql.connector.Error as error:
                print(error)
                sys.exit(1)  
            
        dbConnection.connection.close()
        return (hoursWorkedR, teamHourI)