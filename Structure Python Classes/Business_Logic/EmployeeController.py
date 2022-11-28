from Data_Objects.Employee import Employee
from Persistence.EmployeePersistenceService import EmployeePersistenceService
"""
Employee Controller that Employee Interface will call for logic of process
"""
class EmployeeController:
    def __init__(self):
        pass

    """
    Logic to update employee information
    """
    @staticmethod
    def updateEmployeeInformation(employee: Employee):
        EmployeePersistenceService.updateEmployeeInformation(employee)
        pass

    """
    Logic to log an employees work hours
    """
    @staticmethod
    def logWorkHours(employee: Employee, workType, workTime):
        EmployeePersistenceService.logWorkHours(employee, workType, workTime)
        pass

    """
    Get Employee by Id
    """
    @staticmethod
    def getEmployeeById(employeeId) -> Employee:
        return EmployeePersistenceService.searchEmployeeById(employeeId)