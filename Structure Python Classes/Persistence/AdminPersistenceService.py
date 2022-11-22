from Employee import Employee

"""
Admin Persistence Service receives calls from Admin Controller and interacts with the database
"""
class AdminPersistenceService:
    def __init__(self):
        pass

    """
    Update Employee Role
    """
    @staticmethod
    def setEmployeeRole(employeeId, role):
        pass

    """
    Register new Employee
    """
    @staticmethod
    def registerNewEmployee(employee: Employee):
        pass

    """
    Make active employee inactive
    """
    @staticmethod
    def setEmployeeInactive(employeeId):
        pass