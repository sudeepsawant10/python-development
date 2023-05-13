
class demo:
    def __init__(self):
        self._b = 20  # protected
        self.__c = 30  # private

    def get(self):
        # return self._b
        return self.__c

    def set(self, x):
        # self._b = x
        self.__c = x


d = demo()
print(d.get())
d.set(40)
print(d.get())
