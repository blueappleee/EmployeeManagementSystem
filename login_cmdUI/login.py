import UI
import pyfiglet
def main():
    ascii_banner = pyfiglet.figlet_format("Employee management system")
    print(ascii_banner)
    uid = input("enter user ID: ")
    pwd = input("enter user password: ")
    #query uid and pwd 
    #left to implement.....
    #if either not found,notify then ask for inupt
    #if not match, notify then ask for input
    userAccessLevel = "something" #base on the query info
    UI = UI.UI_generator.generate(userAccessLevel,uid)
    
  

if __name__=="__main__":
    main()