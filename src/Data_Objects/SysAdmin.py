from Data_Objects.Employee import Employee
from datetime import datetime
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

    """
    Create a SysAdmin employee with only required parameters and setting rest to default values
    """
    @classmethod
    def createMinEmployee(cls, employeeId, password, fName, lName, salary, sickDaysYearly,
                          vacationDaysYearly, workEmail, ssn, position='Employee', startDate=None,
                          teamId=None, managerId=None, birthDate=None, address=None, phoneNumber=None,
                          personalEmail=None, directDepositNumber=None):
        cls.employeeId = employeeId
        cls.password = password
        # Admin employee is set as 'adm' empType
        cls.empType = 'adm'
        cls.teamId = teamId
        cls.managerId = managerId
        cls.fName = fName
        cls.lName = lName
        cls.salary = salary
        cls.position = position

        # Check if start date is set otherwise set to current date
        setStartDate = startDate
        if setStartDate is None:
            date = datetime.now()
            setStartDate = date.strftime("%Y") + '-' + date.strftime("%m") + '-' + date.strftime("%d")
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
