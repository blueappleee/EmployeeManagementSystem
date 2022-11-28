from generalUI import employee_UI
from managerUI import manager_UI
from adminUI import admin_UI
import sys


class UI_generator():
    def generate(self, level, uid):
        generator = get_generator(level)
        return generator(uid)

"""
Generate methods for the factory
"""
def get_generator(level):
    if level == 'E':
        return generate_employeeUI
    elif level == 'M':
        return generate_managerUI
    elif level == 'A':
        return generate_adminUI
    else:
        print(f"Undefined access level, please contact system admin.")
        sys.exit(0)
def generate_employeeUI(uid):#employee factory
    return employee_UI(uid)
def generate_managerUI(uid):#manager factory
    return manager_UI(uid)
def generate_adminUI(uid):#admin factory
    return admin_UI(uid)