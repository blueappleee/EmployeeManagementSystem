import  sys, pyfiglet, signal,os
from Business_Logic import EmployeeController as ec
from UI_factory import UI_generator
from getpass import getpass


def Destruct(signum,frame):
    print("\nlog out.")
    ascii_banner = pyfiglet.figlet_format("Bye!")
    print(ascii_banner)
    sys.exit(0)

signal.signal(signal.SIGINT,Destruct)

def main():
    ascii_banner = pyfiglet.figlet_format("System Login")
    print(ascii_banner)
    uid = input("enter user ID: ")
    pwd = getpass("enter user password: ")
    employee  = ec.EmployeeController.getEmployeeById(uid)
    os.system('cls' if os.name == 'nt' else 'clear')
    """
    query uid and pwd 
    left to implement.....
    if either not found,notify then ask for inupt
    if not match, notify then ask for input
    """
    userAccessLevel = "E" #shuold be employee.level something
    UIgenerate = UI_generator()
    cmdUI = UIgenerate.generate(employee.empType,uid)
    cmdUI.assignDataObject(employee)
    cmdUI.cmd_UI()
    


if __name__=="__main__":
    main()