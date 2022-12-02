from datetime import datetime
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

    """
    Create an Employee with only required parameters and setting rest to default values. Helper for 
    creating a new Employee.
    """
    @classmethod
    def createMinEmployee(cls, employeeId, password, fName, lName, salary, sickDaysYearly,
                          vacationDaysYearly, workEmail, ssn, position='Employee', startDate=None,
                          teamId=None, managerId=None, birthDate=None, address=None, phoneNumber=None,
                          personalEmail=None, directDepositNumber=None):
        cls.employeeId = employeeId
        cls.password = password
        # Regular employee is set as 'reg' empType
        cls.empType = 'reg'
        cls.teamId = teamId
        cls.managerId = managerId
        cls.fName = fName
        cls.lName = lName
        cls.salary = salary
        cls.position = position

        # Check if start date is set otherwise set to current date
        setStartDate = startDate
        if setStartDate is None:
            currDate = datetime.now()
            setStartDate = currDate.strftime("%Y") + '-' + currDate.strftime("%m") + '-' + currDate.strftime("%d")
        cls.startDate = setStartDate

        cls.birthDate = birthDate
        cls.sickDaysYearly = sickDaysYearly
        cls.sickDaysRemaining = sickDaysYearly
        cls.vacationDaysYearly = vacationDaysYearly
        cls.vacationDaysRemaining = vacationDaysYearly
        cls.address = address
        cls.phoneNumber = phoneNumber
        cls.workEmail = workEmail
        cls.personalEmail = personalEmail
        cls.directDepositNumber = directDepositNumber
        cls.ssn = ssn
        return cls
