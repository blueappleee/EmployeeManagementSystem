from django.db import models

"""
Employee class for methods and attributes an employee has
"""


class Employee:
    # class attributes
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employeeID = models.CharField(max_length=6, null=False, blank=False)  # primary key
    teamID = models.CharField(max_length=4, null=False, blank=False)  # foreign key
    managerID = models.CharField(max_length=6, null=False, blank=False)  # foreign key
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    salary = models.IntegerField(null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=40)
    empType = models.CharField(3)

    sickDaysYearly = models.SmallIntegerField(null=True, blank=True)
    sickDaysRemaining = models.SmallIntegerField(null=True, blank=True)
    vacationDaysYearly = models.SmallIntegerField(null=True, blank=True)
    vacationDaysRemanining = models.SmallIntegerField(null=True, blank=True)
    address = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10)
    workEmail = models.CharField(max_length=40)
    personalEmail = models.CharField(max_length=40)
    directDepositNumber = models.CharField(max_length=15)
    ssn = models.CharField(max_length=9)

    # control the default ordering of records returned when you query this model type
    class Meta:
        ordering = ['-employeeID']

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.position)

    @property
    def full_name(self):
        return "{} {}".format(self.fname, self.lname)
