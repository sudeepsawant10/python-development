# if-elif
"""
a=int(input("Enter a : "))
b=int(input("Enter b: "))
if(a>b):
    print("a is greater than b")
elif(b>a):
    print("b is greater than a")
else:
    print("a and b are equal")
"""

# program for leap year
"""
year = int(input("Enter year: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap Year")
        else:
            print("not a leap year")
else:
    print("Not a leap year!")
"""

# Leap year using logical operator
# year = int(input("Enter year: "))
# if(year%4==0 and (year%100!=0 or year%400==0)):
#     print("Leap year")
# else:
#     print("Not a leap year")

# #using ternery form (inline)
# print("leap year") if(year%4==0 and (year%100!=0 or year%400==0)) else print("Not a leap year")

list1 = ["sudeep", 32, "mumbai", 400078]

data = 32
if data in list1:
    print(data, " is present in list1")

data = 42
if data not in list1:
    print(data, " is not present in list1")
