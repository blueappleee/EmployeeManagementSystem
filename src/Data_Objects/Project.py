"""
Project object stores details of a project including name, id, team currently working on, and status
"""
class Project:
    def __init__(self, projectId, name, currentTeamId, status):
        self.projectId = projectId
        self.name = name
        self.currentTeamId = currentTeamId
        self.status = status
