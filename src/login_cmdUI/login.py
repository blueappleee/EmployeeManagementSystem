import  sys, pyfiglet, signal,os,hashlib
sys.path.append('../src')
import Business_Logic.EmployeeController as ec
from UI_factory import UI_generator
from getpass import getpass


def Destruct(signum,frame):
    print("\nlog out.")
    ascii_banner = pyfiglet.figlet_format("Bye!")
    print(ascii_banner)
    sys.exit(0)

signal.signal(signal.SIGINT,Destruct)

def login_session():
    uid = input("enter user ID: ")
    pwd = getpass("enter user password: ").encode()
    pwd = hashlib.md5(pwd).hexdigest()
    return uid, pwd

def main():
    ascii_banner = pyfiglet.figlet_format("System Login")
    print(ascii_banner)
    uid, pwd = login_session()
    employee  = ec.EmployeeController.getEmployeeById(uid)
    while str(employee.password) != pwd:
        print('Invalid UserID or Password, Please try again.')
        uid, pwd = login_session()
        pwd = ''
        employee  = ec.EmployeeController.getEmployeeById(uid)
    os.system('cls' if os.name == 'nt' else 'clear')
    """
    query uid and pwd 
    left to implement.....
    if either not found,notify then ask for inupt
    if not match, notify then ask for input
    """
    userAccessLevel = employee.empType 
    UIgenerate = UI_generator()
    cmdUI = UIgenerate.generate(userAccessLevel,employee)
    cmdUI.welcome(employee.fName)
    cmdUI.cmd_UI()
    


if __name__=="__main__":
    main()