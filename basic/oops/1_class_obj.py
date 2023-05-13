"""
class methods alweys take self argument
"""


class Student:
    """"self=> To access variables outside functions """

    def getData(self):
        print("Get data")


a = Student()
a.getData()
