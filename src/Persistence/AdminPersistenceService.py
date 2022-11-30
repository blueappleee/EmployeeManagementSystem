from Data_Objects.Employee import Employee
from Data_Objects.SysAdmin import SysAdmin
from Data_Objects.Team import Team
from Data_Objects.Project import Project

"""
Admin Persistence Service receives calls from Admin Controller and interacts with the database
"""
class AdminPersistenceService:
    def __init__(self):
        pass
        
    def addQuotes(attribute):
        if attribute is not None and attribute != "NULL":
            retstr = '"' + attribute + '"'
            
        else:
            retstr = 'NULL'
            
        return retstr

    """
    Search for admin by id to return
    """
    @staticmethod
    def searchAdminById(adminId) -> SysAdmin:
        cur = dbConnection.connection.cursor()

        try:
            query='SELECT * FROM employee WHERE employeeID=' + self.self.addQuotes(employeeId) + ''
            cur.execute(query)
            result=cur.fetchall()
            sysAdmin = SysAdmin(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9],
                 result[10], result[11], result[12], result[13], result[14],
                 result[15], result[16], result[17], result[18], result[19], result[20])
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        dbConnection.connection.close()
        
        return sysAdmin

    """
    Update Employee Role
    """
    @staticmethod
    def setEmployeeRole(employeeId, role):
        try:
            query='UPDATE employee SET position=' + self.addQuotes(role) + ' WHERE employeeID=' + self.self.addQuotes(employeeId) + ''
            cur.execute(query)
            posResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
            
        return posResult

    """
    Register new Employee
    """
    @staticmethod
    def registerNewEmployee(employee: Employee):
        cur = dbConnection.connection.cursor()
        teamI=""
        manI=""
        #update usecase, this doesnt need to include setEmployeeRoel??
        try:
            query='INSERT INTO employee (employeeID, password, empType, teamID, managerID, fname, lname, salary, position, startDate, birthDate, sickDaysYearly, sickDaysRemaining, vacationDaysYearly, vacationDaysRemaining, address, phonenumber, workEmail, personalEmail, directDepositNumber, ssn) VALUES ("'
                   + self.addQuotes(employee.employeeId) + ', ' + self.addQuotes(employee.password) + ', ' + self.addQuotes(employee.empType) + ', ' + self.addQuotes(employee.teamId) + ', ' + self.addQuotes(employee.managerId) + ', '
                   + self.addQuotes(employee.fname) + ', ' + self.addQuotes(employee.lname) + ', ' + self.addQuotes(employee.salary) + ', ' + self.addQuotes(employee.position) + ', ' + self.addQuotes(employee.startDate.strftime('%Y-%m-%d')) + ', '
                   + self.addQuotes(employee.birthDate.strftime('%Y-%m-%d')) + ', ' + self.addQuotes(employee.sickDaysYearly) + ', ' + self.addQuotes(employee.sickDaysRemaining) + ', ' + self.addQuotes(employee.vacationDaysYearly) + ', '
                   + self.addQuotes(employee.vacationDaysRemaining) + ', ' + self.addQuotes(employee.address) + ', ' + self.addQuotes(employee.phonenumber) + ', ' + self.addQuotes(employee.phonenumber) + ', ' + self.addQuotes(employee.workEmail) + ', '
                   + self.addQuotes(employee.personalEmail) + ', ' + self.addQuotes(employee.directDepositNumber) + ', ' + self.addQuotes(employee.ssn) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            empI=cur.rowcount
        except mysql.connector.Error as error:
            # error if employeeId already taken or not null value isnt set
            print(error)
            return error
            
        if employee.teamId != null:
            try:
                query='INSERT INTO teamMembers (teamID, employeeID) VALUES (' + self.addQuotes(employee.teamId) + ' , ' + self.addQuotes(employee.employeeId) + ')'
                cur.execute(query)
                dbConnection.connection.commit()
                teamI=cur.rowcount
            except mysql.connector.Error as error:
                # error if team doesnt exist
                print(error)
                return error
            
        if employee.managerId != null:
            try:
                query='INSERT INTO empManaged (managerID, employeeID) VALUES (' + self.addQuotes(employee.managerId) + ' , ' + self.addQuotes(employee.employeeId) + ')'
                cur.execute(query)
                dbConnection.connection.commit()
                manI=cur.rowcount
            except mysql.connector.Error as error:
                # error if team doesnt exist
                print(error)
                return error
            
        dbConnection.connection.close()
        return (empI, teamI, manI)

    """
    Make active employee inactive
    """
    @staticmethod 
    def setEmployeeInactive(employeeId):
        try:
            query='DELETE FROM empManaged WHERE employeeID=' + self.addQuotes(employeeId) + ''
            cur.execute(query)
            teamManRowExists = False
            managedResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
            
        try:
            query='DELETE FROM teamMembers WHERE employeeID=' + self.addQuotes(employeeId) + ''
            cur.execute(query)
            memberResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
    
        try:
            query='UPDATE employee SET position="Inactive" WHERE employeeID=' + self.addQuotes(employeeId) + ''
            cur.execute(query)
            posResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
            
        return (managedResult, memberResult, posResult)

    """
    Update Database to assign a manager to a team
    """
    @staticmethod
    def assignManagerToTeam(managerId, teamId):
        # will return error if team doesnt already exist
        cur = dbConnection.connection.cursor()

        try:
            query='UPDATE team SET teamManagerID=' + self.addQuotes(teamId) + ' WHERE teamID=' + self.addQuotes(manager.teamId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            teamI= cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            return error
            
            
        try:
            query='UPDATE employee SET teamID=' + self.addQuotes(teamId) + ' WHERE employeeID=' + self.addQuotes(manager.employeeId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            empI= cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            return error
              
        try:
            query='SELECT * FROM teamMembers WHERE employeeID=' + self.addQuotes(manager.employeeId) + ''
            cur.execute(query)
            teamRowExists = False
            memberResult = cur.fetchall()
            teamMemI=""
            
            for row in memberResult:
                if row[0] != teamId:
                    dropQuery = 'DELETE FROM teamMembers WHERE employeeID=' + self.addQuotes(manager.employeeId) + ' AND teamID=' + self.addQuotes(teamId) + ''
                    cur.execute(sql)
                    dbConnection.connection.commit()
                else:
                    teamRowExists=True
                    
            if teamRowExists==False:
                try:
                    query='INSERT INTO teamMembers (teamID, employeeID) VALUES (' + self.addQuotes(teamId) + ', ' + self.addQuotes(manager.employeeId) +  ')'
                    cur.execute(query)
                    dbConnection.connection.commit()
                    teamMemI = cur.rowcount
                except mysql.connector.Error as error:
                    print(error)
                    return error
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        
        try:
            query='SELECT * FROM teamManaged WHERE managerID=' + self.addQuotes(manager.employeeId) + ''
            cur.execute(query)
            teamManRowExists = False
            managedResult = cur.fetchall()
            teamManI=""
            
            for row in managedResult:
                if row[1] != teamId:
                    dropQuery = 'DELETE FROM teamManaged WHERE managerID=' + self.addQuotes(manager.employeeId) + ' AND teamID=' + self.addQuotes(teamId) + ''
                    cur.execute(sql)
                    dbConnection.connection.commit()
                else:
                    teamManRowExists=True
                    
            if teamManRowExists==False:
                try:
                    query='INSERT INTO teamManaged (managerID, teamID) VALUES (' + self.addQuotes(manager.employeeId) + ', ' + self.addQuotes(teamId) +  ')'
                    cur.execute(query)
                    dbConnection.connection.commit()
                    teamManI = cur.rowcount
                except mysql.connector.Error as error:ject
                    print(error)
                    return error
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
        
        
        dbConnection.connection.close()
        return (teamI, empI, teamMemI, teamManI)

    """
    Create new record in Team table for team with data stored in Team object
    """
    @staticmethod
    def createTeam(team: Team):
        cur = dbConnection.connection.cursor()

        try:
            query='INSERT INTO team (teamID, teamManagerID, teamName, projectID) VALUES ('
                   + self.addQuotes(team.teamId) + ', ' + self.addQuotes(team.teamManagerId) + ', ' + self.addQuotes(team.teamName) + ', ' + self.addQuotes(team.projectId) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            teamI = cur.rowcount
        except mysql.connector.Error as error:
            # potential errors: project needs to exist before adding team with an active project
            print(error)
            return error
            
        # fix this to insert into teamMembers table    
        membersI = []
        if team.teamMembers != []:
            for member in team.teamMembers:
                try:
                    query='INSERT INTO teamMember (teamID, employeeID) VALUES (' + self.addQuotes(team.teamId) + ', ' + self.addQuotes(member) + ')'
                    cur.execute(query)
                    dbConnection.connection.commit()
                    membersI.append(cur.rowcount)
                    
                    query='UPDATE employee SET teamID=' self.addQuotes(team.teamId) + ' WHERE employeeID=' + self.addQuotes(member) + ''
                    cur.execute(query)
                    dbConnection.connection.commit()
                    membersI.append(cur.rowcount)
                except mysql.connector.Error as error:
                    print(error)
                    return error
        
        dbConnection.connection.close()
        return (teamI, membersI)
        
    """
    Create new record in Project table for project with data stored in Project object
    """
    @staticmethod
    def createProject(project: Project):
        cur = dbConnection.connection.cursor()

        try:
            query='INSERT INTO project (projectID, projectName, currentTeamID, projectStatus) VALUES ('
                   + self.addQuotes(project.projectId) + ', ' + self.addQuotes(project.projectName) + ', ' + self.addQuotes(project.currentTeamId) + ', ' + self.addQuotes(project.projectStatus) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            projrows= cur.rowcount
        except mysql.connector.Error as error:
            # potential errors: team does not exist
            print(error)
            return error
            
        
        try:
            query='UPDATE team SET projectID=' + self.addQuotes(project.projectId) + ' WHERE teamID=' + self.addQuotes(project.teamId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            teamI= cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            return error
            
        dbConnection.connection.close()
        return (projrows,teamI)