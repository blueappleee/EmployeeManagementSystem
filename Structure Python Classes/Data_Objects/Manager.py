from Data_Objects.Employee import Employee
"""
Manager class for methods of employee and attributes
"""
class Manager(Employee):
    def __init__(self, employeeId, password, empType, teamId, managerId, fName, lName, salary, position, startDate,
                 birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining,
                 address, phoneNumber, workEmail, personalEmail, directDepositNumber, ssn, employeesManaged,
                 teamManaged):
        super().__init__(self, employeeId, password, empType, teamId, managerId, fName, lName, salary, position,
                         startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly,
                         vacationDaysRemaining,address, phoneNumber, workEmail, personalEmail, directDepositNumber,
                         ssn)
        self.employeesManaged = employeesManaged
        self.teamManaged = teamManaged
