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
    if level == 'E':
        ascii_banner = pyfiglet.figlet_format("Regular Staff Panel")
        print(ascii_banner)
        return generate_employeeUI
    elif level == 'M':
        ascii_banner = pyfiglet.figlet_format("Manager Panel")
        print(ascii_banner)
        return generate_managerUI
    elif level == 'A':
        ascii_banner = pyfiglet.figlet_format("System Admin Panel")
        print(ascii_banner)
        return generate_adminUI
    else:
        print(f"Undefined access level, please contact system admin.")
        sys.exit(0)
def generate_employeeUI(uid):#employee factory
    return employeeUI(uid)
def generate_managerUI(uid):#manager factory
    return managerUI(uid)
def generate_adminUI(uid):#admin factory
    return adminUI(uid)