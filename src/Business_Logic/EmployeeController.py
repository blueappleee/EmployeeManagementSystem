from Data_Objects.Employee import Employee
from Persistence.EmployeePersistenceService import EmployeePersistenceService
import datetime

"""
Employee Controller that Employee Interface will call for logic of process
"""
class EmployeeController:
    """
    Rules for employee table:1. fixed lenth attributes IDs 2.date 3.integer(max value) 4.year(365)
    rest are char vector with upper bound
    """
    Employee_rules = {'employeeID':'fixed', 'teamID':'fixed', 'managerID':'fixed', 
    'password':32, 'empType':3, 'fName':20, 'address':50,
    'lName': 20,'phoneNumber': 10,'workEmail': 40,'personalEmail':40,'directDepositNumber' :21,'ssn':9 , 'position': 40,
    'salary': 'int',                            
    'startDate': 'date','birthDate': 'date',
    'sickDaysRemaining' : 'sint','vacationDaysYearly': 'sint','vacationDaysRemaining' : 'sint', 'sickDaysYearly':'sint'}
    
    fixed_length = {'employeeID':6,'teamID':4,'managerID':6}
    def __init__(self):
        
        self.dataobject = {}

    
    @staticmethod
    def isfixed(input,type):
        fixLength = EmployeeController.fixed_length[type]
        if fixLength == len(input): return True
        return f'Error: wrong attribute({type}) format. Must be exactly{fixLength}.'

    @staticmethod    
    def issint(input,type):
        if input < 365 or input > -365: return True
        return f'Error: wrong attribute({type}) format. Should be a number within (-365,365).'

    @staticmethod
    def isint(input,type):
        if input.isnumeric(): return True
        try: int(input)
        except Exception: return f'Error: The number you entered is not reasonable!'
        return f'Error: wrong attribute({type}) format. Should be a number.'

    @staticmethod
    def isdate(input,type):
        try:
            datetime.datetime.strptime(input, '%Y-%m-%d')
            return True
        except ValueError:
            return f'Error: wrong attribute({type}) format. Should be YYYY-MM-DD with valid date'


    """
    Logic to update employee information
    """
    @staticmethod
    def updateEmployeeInformation(changed, employee: Employee):
        #map each kind of format to its validation function, so can be called directly (not to write if/else)
        rules_func_map = {'fixed': EmployeeController.isfixed, 'int':EmployeeController.isint,'date':EmployeeController.isdate,'sint':EmployeeController.issint}
        
        if changed not in EmployeeController.Employee_rules:
            return  f'Sorry, attribute {changed} not found.'
        if changed not in ['fName','lName','birthDate','phoneNumber','peronalEmail']:#!!!!not sure what else is allowed!!!!
            return f'Sorry, no change permission on attribute {changed}.'

        #at this point, changed attribute must in the format dict:Employee_rules{}
        rule_of_changed = EmployeeController.Employee_rules[changed]
        if not isinstance(rule_of_changed,int):#rule_of_changed falls into the other 4 formats(fixed, int, ssint, date)
            msg = rules_func_map[rule_of_changed](getattr(employee, changed),changed) #get the attribute value, attribute type
            if  msg != True:
                return msg
        else:#only restrict length
            if len(getattr(employee, changed)) > rule_of_changed:
                return f'Illegal input, input length must be no more than {rule_of_changed}.'
        #EmployeePersistenceService.updateEmployeeInformation(employee)
        return f'Success! attribute {changed} has been modified!'

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
    def getEmployeeById(employeeId) -> Employee:#!!!!!!only for testing UI and business logic layer!!!!!
        #self.dataobject = query result
        #return self.dataobject copy
        return Employee(1,1,'E',1,1,'zi','l',11,'senitor','2000/1/1','2000/1/1',
        365,0,0,0,'somewhere','519','43@aa.com','zi@out.com',111,111)
        #return EmployeePersistenceService.searchEmployeeById(employeeId)