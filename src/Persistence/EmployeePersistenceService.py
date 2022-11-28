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
        pass

    """
    Update Employee record in Employee Table
    """
    @staticmethod
    def updateEmployeeInformation(employee: Employee):
        pass

    """
    Update Employee's work hours
    """
    @staticmethod
    def logWorkHours(employee: Employee, workType, workTime):
        pass