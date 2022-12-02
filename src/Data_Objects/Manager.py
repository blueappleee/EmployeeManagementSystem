from src.Data_Objects.Employee import Employee
from datetime import datetime
"""
Manager class for methods of employee and attributes
"""
class Manager(Employee):
    def __init__(self, employeeId, password, empType, teamId, managerId, fName, lName, salary, position, startDate,
                 birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining,
                 address, phoneNumber, workEmail, personalEmail, directDepositNumber, ssn, employeesManaged=None,
                 teamManaged=None):
        # Create Employee attributes
        super().__init__(self, employeeId, password, empType, teamId, managerId, fName, lName, salary, position,
                         startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly,
                         vacationDaysRemaining,address, phoneNumber, workEmail, personalEmail, directDepositNumber,
                         ssn)
        # Optional attributes that can be set after initialization
        self.employeesManaged = employeesManaged
        self.teamManaged = teamManaged

    """
    Create a Manager employee with only required parameters and setting rest to default values. Helper for 
    creating a new manager Employee.
    """
    @classmethod
    def createMinEmployee(cls, employeeId, password, fName, lName, salary, sickDaysYearly,
                          vacationDaysYearly, workEmail, ssn, position='Manager', startDate=None,
                          teamId=None, managerId=None, birthDate=None, address=None, phoneNumber=None,
                          personalEmail=None, directDepositNumber=None):
        cls.employeeId = employeeId
        cls.password = password
        # Manager employee is set as 'mng' empType
        cls.empType = 'mng'
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
        cls.employeesManaged = None
        cls.teamManaged = None
        return cls

    """
    Create a Manager with only required parameters and setting rest to default values. Helper for 
    creating a new Manager, option to set employeesManaged and teamManaged.
    """
    @classmethod
    def createMinManager(cls, employeeId, password, fName, lName, salary, sickDaysYearly,
                          vacationDaysYearly, workEmail, ssn, position='Manager', startDate=None,
                          teamId=None, managerId=None, birthDate=None, address=None, phoneNumber=None,
                          personalEmail=None, directDepositNumber=None, employeesManaged=None, teamManaged=None):
        cls.employeeId = employeeId
        cls.password = password
        # Manager employee is set as 'mng' empType
        cls.empType = 'mng'
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
        cls.employeesManaged = employeesManaged
        cls.teamManaged = teamManaged
        return cls
