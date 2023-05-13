class demo:
    def __init__(self):
        self.a = 1
        self._b = 20  # protected
        self.__c = 30  # private

    def show(self):
        print(self.a)
        print(self._b)
        print(self.__c)

        # return self._b #It will work
        return self.__c  # it also work


d = demo()
d.show()
print("By retruning : ", d.show())
