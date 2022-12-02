"""
Object to store the hours worked by a team on a project
"""
class TeamHoursWorked:
    def __init__(self, teamId, projectId, hourAmount=0):
        self.teamId = teamId
        self.projectId = projectId
        self.hourAmount = hourAmount
