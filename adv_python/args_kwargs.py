"""
1.)*args (Non-Keyword Arguments)

2.)**kwargs (Keyword Arguments)

here keyword menas key pair of key
kwargs deals with dictionary
"""
# *args take data in tuple


# def functionr_print(a, *args):
#     print(a, end=" ")
#     for arg in args:
#         print(arg, end=" ")


# narg = "normalarg"
# names = ["harry", "rohan", "skillf", "love", "Kiran"]
# name = input("Enter your name: ")
# names.append(name)
# functionr_print(narg, *names)

# def my_fun(*args, **kwargss):
#     print("hello ", args, kwargss)


# my_fun("abc", 123, "pqr", "xyz", abc=123, name="sudeep")

# *arg takes only non-keyworkd n number of parameters
# application can take n no. of input from user and pass it to this
# def arg_fun(a, *args):
#     print("hello ", a, args)


# arg_fun("a", 1, "a", "b")
# kwargs will take key arguments
# args will take only normal arguments
def foo(required, *args, **kwargs):
    if required:
        print("This is required ", required)
    if args:
        print("This is args = ", args)
    if kwargs:
        print("This is kwargs", kwargs)


foo(1, 2)
foo(1, "hello")
foo(1, "hello", 2, 3, 4)
foo(1, "hello", 2, 3, 4, abc=5)


foo(1)


# Python program to illustrate
# *kargs for variable number of keyword arguments

def myFun(**kwargs):
    # for key, value in kwargs.items():
    #     print("%s == %s" % (key, value))
    print(kwargs)
    print("Accessing only id key : ", kwargs['id'])
    print("Your username: ", kwargs['username'])
    context={'id': kwargs['id'], 'username': kwargs['username']}
    return context

# Driver code
# myFun(first='Geeks', mid='for', last='Geeks')

#we are assigning and passing these is not key pair
myFun(id=1, username='sudeep10')
dic1 = myFun(id=2, username='neel' )
print(dic1)
print(dic1['username'])
