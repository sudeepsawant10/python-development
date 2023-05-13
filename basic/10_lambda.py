# normal function
# def double(x):
#     return x**x

# print(double(2))

# USING LAMBDA anonomous funtion
def a(x): return x**x
def b(a, b): return a+b
# origingal c = lambda a,b: a-b it vscode convert it into this form:
def c(a, b): return a-b


# print(a(2))
# print("Addition = ", b(50, 75))

# # problem squaring the list
# list1 = [1, 2, 3, 4, 5, 6, 7]
# # using map for lambda function
# a = list(map(lambda x: x**2, list1))
# print(a)
# print(list1)

# Use of FILLTER in lambda
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(lambda x: (x % 2 == 0), list2))
print(a)
