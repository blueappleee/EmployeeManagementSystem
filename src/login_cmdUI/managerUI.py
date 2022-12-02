from generalUI import employeeUI
from generalUI import input_shoe_be_num,isdate
from Business_Logic.ManagerController import ManagerController

class managerUI(employeeUI):
    def __init__(self, uid):
        super().__init__(uid)
        self.command_dict['assigne'] = self.assign_team
        self.command_dict['assignt'] = self.assign_project
        self.command_dict['correct'] = self.correct_hours
        self.command_dict['teamsum'] = self.teamEmployeesSummary
        self.command_dict['workdata'] = self.employeeWorkdata
        self.command_dict['project'] = self.projectDetails
        self.command_dict['remove'] = self.removeEmployee
       
    
    """
    Assign Employee to team
    """
    def assign_team(self,employeeID):
        msg = ManagerController.assignEmployeeToTeam(employeeID,self.dataobject.id, self.dataobject.teamId)
        if msg == None:
            print(f'Assigned employee {employeeID} to your team successfully!')
            return
        print(msg)
    """
    Assign Team to Project
    """
    def assign_project(self,projectID):
        msg = ManagerController.assignTeamProject(projectID, self.dataobject.teamId)
        if msg == None:
            print(f'Assigned project {projectID} to your team successfully!')
            return
        print(msg)
    """
    correct a team employee's work hours
    """
    def correct_hours(self,empID):
        while(worktype == ' '): worktype = input("Please enter a work type: ")
        hours = input("Enter the correct hours: ")
        hours = input_shoe_be_num(hours,'hours')
        date = input("Enter the date(YYYY-MM-DD) you wanna correct")
        date = isdate(date)
        while date!= True:#check valid date format
            print(date)
            workDate = input("Enter a valid date(YYYY-MM-DD): ")
            date = isdate(workDate,'work date')
        msg = ManagerController.correctTeamEmployeeWorkHours(empID, worktype, hours, date)
        if msg == None:
            print(f'Corrected work hours for employee{empID} on {date} successfully!')
            return
        print(msg)
        
    """
    Get summary stats on team's employees
    """
    def teamEmployeesSummary(self, nonValue):
        emplist = ManagerController.getSummaryTeamEmployeeData(self.dataobject.teamId)
        if isinstance(emplist, str):
            print(emplist)
            return
        for emp in emplist:
            print(emp)
            
    """
    Get Specific Team Employee's work related data
    """
    def employeeWorkdata(self,employeeID):
        datalist = ManagerController.getTeamEmployeeWorkData(self.dataobject.teamId, employeeID)
        if isinstance(datalist, str):
            print(datalist)
            return
        for data in datalist:
            print(data)
        #and present to the cmd
    """
    Get project details
    """
    def projectDetails(self,project):
        p = ManagerController.getProjectDetails(project)
        print(p)
        
    """
    Remove Employee from team
    """
    def removeEmployee(self,employeeID):
        msg = ManagerController.removeEmployeeFromTeam(self.dataobject.teamId, employeeID)
        if msg == None:
            print(f'Removed employee{employeeID} from your team successfully!')
            return
        print(msg)
        

    def welcome(self,name):
        print(f'Hi, Manager {name}. Welcome!')
        print(
"""You are loging in with manager priviliges, you can enter:
update      *attributes = [fName/lName/birthDate/phoneNumber/personalEmail]   To update your personal Info
report      *worktype = [something not sure]    To log your working hours
assigne     #employeeID                         To assign an employee to your team
assignt     #projectID                          To assign your team to a project
correct     #hours                              To correct the work hours for your team
teamsum                                         To get the working Info summary of your team
workdata    #employeeID                         To get working Info summary of the employee
project     #projectID                          To get the project details
remove      #employeeID                         To remove a employee from your team
When type your command, Words start with * must be replaced by one of the keywords in []
Type exit to logout
Words start with # must be replaced by a valid number""")
