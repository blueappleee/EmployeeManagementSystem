from Data_Objects.Employee import Employee
"""
Employee Persistence Service receives calls from Employee Controller and interacts with the database
"""
class EmployeePersistenceService:
    def __init__(self):
        pass
    
    def addQuotes(attribute):
        if attribute is not None and attribute != "NULL":
            retstr = '"' + attribute + '"'
            
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
            query='SELECT * FROM employee WHERE employeeID=' + self.addQuotes(employeeId) + ''
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
            query='UPDATE employee SET password=' + self.addQuotes(employee.password)
            + ', empType=' + self.addQuotes(employee.empType)
            + ', teamID=' + self.addQuotes(employee.teamId)
            + ', managerID=' + self.addQuotes(employee.managerId)
            + ', fname=' + self.addQuotes(employee.fname)
            + ', lname=' + self.addQuotes(employee.lname)
            + ', salary=' + self.addQuotes(employee.salary)
            + ', position=' + self.addQuotes(employee.position)
            + ', startDate=' + self.addQuotes(employee.startDate)
            + ', birthDate=' + self.addQuotes(employee.birthDate)
            + ', sickDaysYearly=' + self.addQuotes(employee.sickDaysYearly)
            + ', sickDaysRemaining=' + self.addQuotes(employee.sickDaysRemaining)
            + ', vacationDaysYearly=' + self.addQuotes(employee.vacationDaysYearly)
            + ', vacationDaysRemaining=' + self.addQuotes(employee.vacationDaysRemaining)
            + ', address=' + self.addQuotes(employee.address)
            + ', phonenumber=' + self.addQuotes(employee.phonenumber)
            + ', workEmail=' + self.addQuotes(employee.workEmail)
            + ', personalEmail=' + self.addQuotes(employee.personalEmail)
            + ', directDepositNumber=' + self.addQuotes(employee.directDepositNumber)
            + ', ssn=' + self.addQuotes(employee.ssn) + ' WHERE employeeID=' + self.addQuotes(employee.employeeId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            empU=cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
          
        if employee.teamId != null:
            try:
                query='SELECT * FROM teamMembers WHERE employeeID=' + self.addQuotes(employee.employeeId) + ''
                cur.execute(query)
                teamRowExists = False
                memberResult = cur.fetchall()
                teamMemI=""
                
                for row in memberResult:
                    if row[0] != teamId:
                        dropQuery = 'DELETE FROM teamMembers WHERE employeeID=' + self.addQuotes(employee.employeeId) + ' AND teamID=' + self.addQuotes(employee.teamId) + ''
                        cur.execute(sql)
                        dbConnection.connection.commit()
                    else:
                        teamRowExists=True
                        
                if teamRowExists==False:
                    try:
                        query='INSERT INTO teamMembers (teamID, employeeID) VALUES (' + self.addQuotes(employee.teamId) + ', ' + self.addQuotes(employee.employeeId) +  ')'
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
                query='SELECT * FROM empManaged WHERE employeeID=' + self.addQuotes(employee.employeeId) + ''
                cur.execute(query)
                teamRowExists = False
                managedResult = cur.fetchall()
                managedI=""
                
                for row in managedResult:
                    if row[0] != employee.managerId:
                        dropQuery = 'Delete FROM empManaged WHERE employeeID=' + self.addQuotes(employee.employeeId) + ' AND managerID=' + self.addQuotes(employee.managerId) + ''
                        cur.execute(sql)
                        dbConnection.connection.commit()
                    else:
                        teamRowExists=True
                        
                if teamRowExists==False:
                    try:
                        query='INSERT INTO empManaged (managerID, employeeID) VALUES (' + self.addQuotes(employee.managerId) + ' , ' self.addQuotes(employee.employeeId) + ')'
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
            query='INSERT INTO hoursWorked ("employeeID", "hourType", "hourAmount", "workDate") VALUES (' + self.addQuotes(employee.employeeId) + ', ' + self.addQuotes(workType) + ', ' + self.addQuotes(workTime) + ', ' + self.addQuotes(workDate) + ')'
            cur.execute(query)
            mydb.commit()
            hoursWorkedR = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            return error
            
        if employee.teamId != null:
            try:
                query='SELECT projectID FROM team WHERE teamID=' + self.addQuotes(employee.teamId) + ''
                cur.execute(query)
                projectIDR=cur.fetchall()
                projectID=projectIDR[0]

            except mysql.connector.Error as error:
                print(error)
                sys.exit(1)
        
            try:
                query='SELECT * FROM teamHoursWorked WHERE teamID=' + self.addQuotes(employee.teamId) + ' AND projectID=' + self.addQuotes(projectID) + ''
                cur.execute(query)
                teamRowExists = False
                teamHoursResult = cur.fetchall()
                teamHourI=""
                
                if teamHoursResult = []:
                    try:
                        query='INSERT INTO teamHoursWorked (teamID, projectID, hourAmount) VALUES (' + self.addQuotes(employee.teamId) + ', ' + self.addQuotes(projectID) + ', ' + self.addQuotes(workTime) + ')'
                        cur.execute(query)
                        dbConnection.connection.commit()
                        teamHourI = cur.rowcount
                    except mysql.connector.Error as error:
                        print(error)
                        return error
                else:
                    newHours = int(teamHoursResult[2]) + int(hourAmount)
                    try:
                        query='UPDATE teamHoursWorked set hourAmount=' + self.addQuotes(newHours) + ' WHERE teamID=' + self.addQuotes(employee.teamId) + ' AND projectID=' + self.addQuotes(projectID) +  ''
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