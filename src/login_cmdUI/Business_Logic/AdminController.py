from Data_Objects.Employee import Employee
from Persistence.AdminPersistenceService import AdminPersistenceService

"""
Admin Controller that Admin Interface will call for logic of process
"""
class AdminController:
    def __init__(self):
        pass

    """
    Set Employee Role
    """
    @staticmethod
    def setEmployeeRole(employeeId, role):
        AdminPersistenceService.setEmployeeRole(employeeId, role)
        pass

    """
    Register new Employee
    """
    @staticmethod
    def registerNewEmployee(employee: Employee):
        AdminPersistenceService.registerNewEmployee(employee)
        pass

    """
    Make active employee inactive
    """
    @staticmethod
    def setEmployeeInactive(employeeId):
        AdminPersistenceService.setEmployeeInactive(employeeId)
        pass