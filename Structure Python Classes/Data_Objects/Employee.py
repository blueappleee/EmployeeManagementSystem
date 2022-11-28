"""
Employee class for methods and attributes an employee has
"""
class Employee:
    def __init__(self, employeeId, password, empType, teamId, managerId, fName, lName, salary, position, startDate,
                 birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining,
                 address, phoneNumber, workEmail, personalEmail, directDepositNumber, ssn):
        self.employeeId = employeeId
        self.password = password
        self.empType = empType
        self.teamId = teamId
        self.managerId = managerId
        self.fName = fName
        self.lName = lName
        self.salary = salary
        self.position = position
        self.startDate = startDate
        self.birthDate = birthDate
        self.sickDaysYearly = sickDaysYearly
        self.sickDaysRemaining = sickDaysRemaining
        self.vacationDaysYearly = vacationDaysYearly
        self.vacationDaysRemaining = vacationDaysRemaining
        self.address = address
        self.phoneNumber = phoneNumber
        self.workEmail = workEmail
        self.personalEmail = personalEmail
        self.directDepositNumber = directDepositNumber
        self.ssn = ssn
