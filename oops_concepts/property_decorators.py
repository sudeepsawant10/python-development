"""
Dunder/magic method
- inbuilt special method which we can override 

"""

class Employee:
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.email = fname + lname + "@gmail.com"
        Employee.no_of_employees +=1
    def increase(self):
        self.salary = int(self.salary  +self.increment)
    # working as attribute
    @property
    def email(self):    
        return self.fname + self.lname + "@gmail.com"
    
    @email.setter
    def email(self, email_ip):
        name_list = email_ip.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount
    
    @classmethod
    def from_str(cls,emp_string):
        fname, Iname, salary =  emp_string.split("-")
        return cls(fname, lname, salary)
    @staticmethod
    def isopen(day):
        if day == "sunday":
            return false
        else:
            return True

    # dunder method
    def __repr__(self):
        return "Employee {}, {}, with salary {}".format(self.fname, self.lname, self.salary)
if __name__ == '__main__':
    harry = Employee("harry", "jackson", 99000)
    rohan = Employee("rohan", "doe", 19000)
    print(harry.email, rohan.email)
    rohan.lname = "khanna"
    print(harry.email, rohan.email)
    rohan.email = "khanna.rohan@gmail.com" #cannot assign to function call
    print(rohan.email)
    print(rohan)