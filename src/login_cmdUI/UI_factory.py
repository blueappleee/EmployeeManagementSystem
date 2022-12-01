from generalUI import employeeUI
from managerUI import managerUI
from adminUI import adminUI
import sys,pyfiglet


class UI_generator():
    def generate(self, level, uid):
        generator = get_generator(level)
        return generator(uid)

"""
Generate methods for the factory
"""
def get_generator(level):
    if level == 'reg':
        ascii_banner = pyfiglet.figlet_format("Regular Staff Panel")
        print(ascii_banner)
        return generate_employeeUI
    elif level == 'mng':
        ascii_banner = pyfiglet.figlet_format("Manager Panel")
        print(ascii_banner)
        return generate_managerUI
    elif level == 'adm':
        ascii_banner = pyfiglet.figlet_format("System Admin Panel")
        print(ascii_banner)
        return generate_adminUI
    else:
        print(f"Undefined access level, please contact system admin.")
        sys.exit(0)
def generate_employeeUI(dataobject):#employee factory
    return employeeUI(dataobject)
def generate_managerUI(dataobject):#manager factory
    return managerUI(dataobject)
def generate_adminUI(dataobject):#admin factory
    return adminUI(dataobject)