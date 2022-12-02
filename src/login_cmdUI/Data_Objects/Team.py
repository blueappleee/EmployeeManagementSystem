"""
Team object stores details of a team including name, id, list of members, manager id, and assigned project
"""
class Team:
    def __init__(self, teamId, teamMembers=[], managerId=None, projectId=None, name='Unassigned'):
        self.teamId = teamId
        self.teamMembers = teamMembers
        self.managerId = managerId
        self.projectId = projectId
        self.name = name
