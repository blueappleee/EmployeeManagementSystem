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
        if attribute != NULL:
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
            query='SELECT * FROM employee WHERE employeeID=' + addQuotes(employeeId) + ''
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
            query='UPDATE employee SET position=' + addQuotes(role) + ' WHERE employeeID=' + addQuotes(employeeId) + ''
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
                   + addQuotes(employee.employeeId) + ', ' + addQuotes(employee.password) + ', ' + addQuotes(employee.empType) + ', ' + addQuotes(employee.teamId) + ', ' + addQuotes(employee.managerId) + ', '
                   + addQuotes(employee.fname) + ', ' + addQuotes(employee.lname) + ', ' + addQuotes(employee.salary) + ', ' + addQuotes(employee.position) + ', ' + addQuotes(employee.startDate.strftime('%Y-%m-%d')) + ', '
                   + addQuotes(employee.birthDate.strftime('%Y-%m-%d')) + ', ' + addQuotes(employee.sickDaysYearly) + ', ' + addQuotes(employee.sickDaysRemaining) + ', ' + addQuotes(employee.vacationDaysYearly) + ', '
                   + addQuotes(employee.vacationDaysRemaining) + ', ' + addQuotes(employee.address) + ', ' + addQuotes(employee.phonenumber) + ', ' + addQuotes(employee.phonenumber) + ', ' + addQuotes(employee.workEmail) + ', '
                   + addQuotes(employee.personalEmail) + ', ' + addQuotes(employee.directDepositNumber) + ', ' + addQuotes(employee.ssn) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            empI=cur.rowcount
        except mysql.connector.Error as error:
            # error if employeeId already taken or not null value isnt set
            print(error)
            return error
            
        if employee.teamId != null:
            try:
                query='INSERT INTO teamMembers (teamID, employeeID) VALUES (' + addQuotes(employee.teamId) + ' , ' + addQuotes(employee.employeeId) + ')'
                cur.execute(query)
                dbConnection.connection.commit()
                teamI=cur.rowcount
            except mysql.connector.Error as error:
                # error if team doesnt exist
                print(error)
                return error
            
        if employee.managerId != null:
            try:
                query='INSERT INTO empManaged (managerID, employeeID) VALUES (' + addQuotes(employee.managerId) + ' , ' + addQuotes(employee.employeeId) + ')'
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
            query='DELETE FROM empManaged WHERE employeeID=' + addQuotes(employeeId) + ''
            cur.execute(query)
            teamManRowExists = False
            managedResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
            
        try:
            query='DELETE FROM teamMembers WHERE employeeID=' + addQuotes(employeeId) + ''
            cur.execute(query)
            memberResult = cur.rowcount
            
        except mysql.connector.Error as error:
            print(error)
            sys.exit(1)
    
        try:
            query='UPDATE employee SET position="Inactive" WHERE employeeID=' + addQuotes(employeeId) + ''
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
            query='UPDATE team SET teamManagerID=' + addQuotes(teamId) + ' WHERE employeeID=' + addQuotes(manager.employeeId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            teamI= cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            return error
            
            
        try:
            query='UPDATE employee SET teamID=' + addQuotes(teamId) + ' WHERE employeeID=' + addQuotes(manager.employeeId) + ''
            cur.execute(query)
            dbConnection.connection.commit()
            empI= cur.rowcount
        except mysql.connector.Error as error:
            print(error)
            return error
              
        try:
            query='SELECT * FROM teamMembers WHERE employeeID=' + addQuotes(manager.employeeId) + ''
            cur.execute(query)
            teamRowExists = False
            memberResult = cur.fetchall()
            teamMemI=""
            
            for row in memberResult:
                if row[0] != teamId:
                    dropQuery = 'DELETE FROM teamMembers WHERE employeeID=' + addQuotes(manager.employeeId) + ' AND teamID=' + addQuotes(teamId) + ''
                    cur.execute(sql)
                    dbConnection.connection.commit()
                else:
                    teamRowExists=True
                    
            if teamRowExists==False:
                try:
                    query='INSERT INTO teamMembers (teamID, employeeID) VALUES (' + addQuotes(teamId) + ', ' + addQuotes(manager.employeeId) +  ')'
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
            query='SELECT * FROM teamManaged WHERE managerID=' + addQuotes(manager.employeeId) + ''
            cur.execute(query)
            teamManRowExists = False
            managedResult = cur.fetchall()
            teamManI=""
            
            for row in managedResult:
                if row[1] != teamId:
                    dropQuery = 'DELETE FROM teamManaged WHERE managerID=' + addQuotes(manager.employeeId) + ' AND teamID=' + addQuotes(teamId) + ''
                    cur.execute(sql)
                    dbConnection.connection.commit()
                else:
                    teamManRowExists=True
                    
            if teamManRowExists==False:
                try:
                    query='INSERT INTO teamManaged (managerID, teamID) VALUES (' + addQuotes(manager.employeeId) + ', ' + addQuotes(teamId) +  ')'
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
        return (empI, teamMemI, teamManI)

    """
    Create new record in Team table for team with data stored in Team object
    """
    @staticmethod
    def createTeam(team: Team):
        cur = dbConnection.connection.cursor()

        try:
            query='INSERT INTO team (teamID, teamManagerID, teamName, projectID) VALUES ('
                   + addQuotes(team.teamId) + ', ' + addQuotes(team.teamManagerId) + ', ' + addQuotes(team.teamName) + ', ' + addQuotes(team.projectId) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            teamI = cur.rowcount
        except mysql.connector.Error as error:
            # potential errors: project needs to exist before adding team with an active project
            print(error)
            return error
            
        membersI = []
        for member in team.teamMembers:
            try:
                query='INSERT INTO team (teamID, teamManagerID, teamName, projectID) VALUES ('
                       + addQuotes(team.teamId) + ', ' + addQuotes(team.teamManagerID) + ', ' + addQuotes(team.teamName) + ', ' + addQuotes(team.projectId) + ')'
                cur.execute(query)
                dbConnection.connection.commit()
                membersI.append(cur.rowcount)
            except mysql.connector.Error as error:
                # potential errors: project needs to exist before adding team with an active project
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
                   + addQuotes(project.projectId) + ', ' + addQuotes(project.projectName) + ', ' + addQuotes(project.currentTeamId) + ', ' + addQuotes(project.projectStatus) + ')'
            cur.execute(query)
            dbConnection.connection.commit()
            projrows= cur.rowcount
        except mysql.connector.Error as error:
            # potential errors: team does not exist
            print(error)
            return error
            
        # TODO team if teamID is set
            
        dbConnection.connection.close()
        return projrows