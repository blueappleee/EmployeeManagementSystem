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
            mydb.commit()
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
            
        # do teamMember and empManagerd query as well to ensure set properly    
        dbConnection.connection.close()

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
            
        # need to add to team hours worked
        dbConnection.connection.close()