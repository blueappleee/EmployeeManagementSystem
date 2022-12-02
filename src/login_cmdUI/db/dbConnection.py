import mysql.connector
from mysql.connector import Error

def connectTo_DB():
    #try:
    connection = mysql.connector.connect(host='localhost',
                                             database='empManagementdb',
                                             user='empManagement',
                                             password='cs4471pass')
        #if connection.is_connected():
        #    db_Info = connection.get_server_info()
         #   print("Connected to MySQL Server version ", db_Info)
            #cursor = connection.cursor()
            #cursor.execute("select database();")
            #record = cursor.fetchone()
            #print("You're connected to database: ", record)
    return connection

    #except Error as e:
     #   print("Error while connecting to MySQL", e)
    #finally:
     #   if connection.is_connected():
            #cursor.close()
      #      connection.close()
       #     print("MySQL connection is closed")
            
    


# example of executing a query
def doQuery(conn):
    cur = conn.cursor()

    cur.execute("SELECT fname, lname FROM employee")

    for firstname, lastname in cur.fetchall():
        print(firstname, lastname)
        
connection = connectTo_DB()
