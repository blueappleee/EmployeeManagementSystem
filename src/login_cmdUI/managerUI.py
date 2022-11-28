from generalUI import employee_UI
from generalUI import input_shoe_be_num
from Business_Logic.ManagerController import ManagerController

class manager_UI(employee_UI):
    
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
