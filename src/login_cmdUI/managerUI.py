from generalUI import employeeUI
from generalUI import input_shoe_be_num
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
        print(
"""You are loging in with manager priviliges, you can enter:
update      *attributes = [fName/lName/birthDate/phoneNumber/personalEmail]   To update your personal Info
report      *worktype = [something not sure]    To log your working hours
assigne     #employeeID                         To assign an employee to your team
assignt     #teamID                             To assign toyr team to a project
correct     #hours                              To correct the work hours for your team
teamsum                                         To get the working Info summary of your team
workdata    #employeeID                         To get working Info summary of the employee
project     #projectID                          To get the project details
remove      #employeeID                         To remove a employee from your team
When type your command, Words start with * must be replaced by one of the keywords in []
Type exit to logout
Words start with # must be replaced by a valid number""")
    
    """
    Assign Employee to team
    """
    def assign_team(self,employeeID):
        employeeID = input_shoe_be_num(employeeID)
        ManagerController.assignEmployeeToTeam(employeeID,self.dataobject.id) #this line need further detail for dataobject INFO
    """
    Assign Team to Project
    """
    def assign_project(self,team):
        team = input_shoe_be_num(team)
        projectID = input("enter the project id you wanna assign: ")
        ManagerController.assignTeamProject(projectID,team)
    """
    correct a team employee's work hours
    """
    def correct_hours(self,hours):
        hours = input_shoe_be_num(hours)
        ManagerController.correctTeamEmployeeWorkHours(hours)
    """
    Get summary stats on team's employees
    """
    def teamEmployeesSummary(self,team):
        team = input_shoe_be_num(team)
        ManagerController.getSummaryTeamEmployeeData(team)
    """
    Get Specific Team Employee's work related data
    """
    def employeeWorkdata(self,employeeID):
        employeeID = input_shoe_be_num(employeeID)
        ManagerController.getTeamEmployeeWorkData(employeeID)
        #and present to the cmd
    """
    Get project details
    """
    def projectDetails(self,project):
        project  = input_shoe_be_num(project)
        ManagerController.getProjectDetails(project)
        #and present to the cmd
    """
    Remove Employee from team
    """
    def removeEmployee(self,employeeID):
        employeeID = input_shoe_be_num(employeeID)
        ManagerController.removeEmployeeFromTeam(employeeID)
