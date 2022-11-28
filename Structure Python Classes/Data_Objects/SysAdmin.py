from Data_Objects.Employee import Employee
"""
SysAdmin class for methods and attributes of a SysAdmin
"""
class SysAdmin(Employee):
    def __init__(self, employeeId, password, empType, teamId, managerId, fName, lName, salary, position, startDate,
                 birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining,
                 address, phoneNumber, workEmail, personalEmail, directDepositNumber, ssn):
        super().__init__(self, employeeId, password, empType, teamId, managerId, fName, lName, salary, position,
                         startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly,
                         vacationDaysRemaining,address, phoneNumber, workEmail, personalEmail, directDepositNumber,
                         ssn)
