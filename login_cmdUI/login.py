import UI, sys, pyfiglet, signal

def Destruct(signum,frame):
    print("\nlog out.")
    sys.exit(0)

signal.signal(signal.SIGINT,Destruct)

def main():
    ascii_banner = pyfiglet.figlet_format("Employee management system")
    print(ascii_banner)
    uid = input("enter user ID: ")
    pwd = input("enter user password: ")
    #query uid and pwd 
    #left to implement.....
    #if either not found,notify then ask for inupt
    #if not match, notify then ask for input
    userAccessLevel = "E" #base on the query info
    UIgenerate = UI.UI_generator()
    cmdUI = UIgenerate.generate(userAccessLevel,uid)
    


if __name__=="__main__":
    main()