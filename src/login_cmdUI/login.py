import  sys, pyfiglet, signal
from Business_Logic import EmployeeController as ec
from UI_factory import UI_generator


def Destruct(signum,frame):
    print("\nlog out.")
    sys.exit(0)

signal.signal(signal.SIGINT,Destruct)

def main():
    ascii_banner = pyfiglet.figlet_format("Employee management system")
    print(ascii_banner)
    uid = input("enter user ID: ")
    pwd = input("enter user password: ")
    employee  = ec.EmployeeController.getEmployeeById(uid)
    """
    query uid and pwd 
    left to implement.....
    if either not found,notify then ask for inupt
    if not match, notify then ask for input
    """
    userAccessLevel = "E" #shuold be employee.level something
    UIgenerate = UI_generator()
    cmdUI = UIgenerate.generate(userAccessLevel,uid)
    cmdUI.assignDataObject(employee)
    cmdUI.cmd_UI()
    


if __name__=="__main__":
    main()