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
        employeeID = input_shoe_be_num(employeeID,'employeeID')
        msg = ManagerController.assignEmployeeToTeam(employeeID,self.dataobject.id) #this line need further detail for dataobject INFO
        if msg == None:
            print(f'Assign employee {employeeID} to your team success!')
            return
        print(msg)
    """
    Assign Team to Project
    """
    def assign_project(self,projectID):
        team = input_shoe_be_num(team,'teamID')
        projectID = input("enter the project id you wanna assign: ")
        msg = ManagerController.assignTeamProject(projectID,team)
        if msg == None:
            print(f'Assign project {employeeID} to your team success!')
            return
        print(msg)
    """
    correct a team employee's work hours
    """
    def correct_hours(self,empID):
        empID = input_shoe_be_num(empID, 'employeeID')
        hours = input("Enter the correct hours: ")
        hours = input_shoe_be_num(hours,'hours')
        date = input("Enter the date(YYYY-MM-DD) you wanna correct")
        date = isdate(date)
        while date!= True:#check valid date format
            print(date)
            workDate = input("Enter a valid date(YYYY-MM-DD): ")
            date = isdate(workDate,'work date')
        msg = ManagerController.correctTeamEmployeeWorkHours(hours)
        if msg == None:
            print(f'Correct work hour for employee{empID} on {date} success!')
            return
        print(msg)
        
    """
    Get summary stats on team's employees
    """
    def teamEmployeesSummary(self,team):
        team = input_shoe_be_num(team,'teamID')
        emplist = ManagerController.getSummaryTeamEmployeeData(team)
        if isinstance(emplist, str):
            print(emplist)
            return
        for emp in emplist:
            print(emp)
            
    """
    Get Specific Team Employee's work related data
    """
    def employeeWorkdata(self,employeeID):
        employeeID = input_shoe_be_num(employeeID,'employeeID')
        datalist = ManagerController.getTeamEmployeeWorkData(employeeID)
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
        project  = input_shoe_be_num(project,'projectID')
        p = ManagerController.getProjectDetails(project)
        print(p)
        
    """
    Remove Employee from team
    """
    def removeEmployee(self,employeeID):
        employeeID = input_shoe_be_num(employeeID,'employeeID')
        msg = ManagerController.removeEmployeeFromTeam(employeeID)
        if msg == None
            print(f'remove employee{empID} from your team success!')
            return
        print(msg)
    def welcome(self,name):
        print(f'Hi, Manager {name}. Welcome!')
        print(
"""You are loging in with manager priviliges, you can enter:
update      *attributes = [fName/lName/birthDate/phoneNumber/personalEmail]   To update your personal Info
report      *worktype = [something not sure]    To log your working hours
assigne     #employeeID                         To assign an employee to your team
assignt     #projectID                          To assign toyr team to a project
correct     #hours                              To correct the work hours for your team
teamsum                                         To get the working Info summary of your team
workdata    #employeeID                         To get working Info summary of the employee
project     #projectID                          To get the project details
remove      #employeeID                         To remove a employee from your team
When type your command, Words start with * must be replaced by one of the keywords in []
Type exit to logout
Words start with # must be replaced by a valid number""")
