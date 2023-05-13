# If we didn't give self for variable it will give u error as not defined
class Student:
    """"self=> To access variables outside functions """

    def getData(self):
        self.Name = "summer"
        self.id1 = 13

    def showData(self):
        print(self.Name)
        # print(id1) #Global id is not defined
        print(self.id1)


a = Student()
a.getData()
a.showData()
