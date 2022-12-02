from datetime import datetime
"""
Object to store the hours worked, date, hour type for an employee
"""
class TeamHoursWorked:
    def __init__(self, employeeId, hourType, hourAmount=0, workDate=None):
        self.employeeId = employeeId
        self.hourType = hourType
        self.hourAmount = hourAmount
        setWorkDate = workDate
        if setWorkDate is None:
            currDate = datetime.now()
            setWorkDate = currDate.strftime("%Y") + '-' + currDate.strftime("%m") + '-' + currDate.strftime("%d")
        self.workDate = setWorkDate
