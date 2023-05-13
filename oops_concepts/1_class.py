# You can create and assign value to instance variable outside of class in python

class Employee:
    # class variable common to all
    # Can be access by objects
    increment_salary = 1.5

    def __init__(self, fname, lname, salary):
        # instance variable belongs to the object(personal)
        # Only accessed by objects
        # self will create or point to object attrubutes(variables)
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    def increase(self):
        self.salary = int(self.salary * Employee.increment_salary)
        pass

    # method can access class variables
    @classmethod
    def change_increment(cls, incr_by):
        cls.change_increment = incr_by

    # above and below are similar
    # def change_increment(incr_by):
    #     Employee.change_increment = incr_by

    # alternative user-defined constructor can be create using class method
    @classmethod
    def from_str(cls, ip_string):
        fname, lname, salary = ip_string.split('-')
        return cls(fname, lname, salary)
    
    # Can be acces using object and also class
    @staticmethod
    def isOpen(day):
        if day == 'sunday':
            return False
        else:
            return True


harry = Employee('harry', 'sharma', 44000)
rohan = Employee('rohan', 'jadhav', 50000)

# harry.increase()    automatic takes self
print(harry.salary)
harry.increase()
print(harry.salary)

Employee.change_increment(1.9)
harry.increase()
print(harry.salary)

# instance using alternative constructor
kiran = Employee.from_str("kiran-rane-50000")
print(kiran.fname, kiran.lname, kiran.salary)

print(Employee.isOpen('sunday'))
print(kiran.isOpen('monday'))
# # To check variables of object
# print(harry.__dict__)

# # creating instance variable outside of class using object
# harry.increment = 90
# print(harry.__dict__)


