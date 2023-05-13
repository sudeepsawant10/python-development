"""
python dosen't support abstract but we can achive it using abc module
Abstract Base Class
- abstract (Dosen't have defination)
- cannot create object of abstract method
What is the use?
- Used in modules
- Used in oops (follow design patterns)




"""
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('Abstract method used')


# com = Computer()
# com.process()

com2 = Laptop()
com2.process()
