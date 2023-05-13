import os
# fname = input("Enter your name: ")
directory = "C:\\Users\\Sudeep\\Desktop\\code\\py tutorial"
# filepath = directory + input("Enter filename: ")
name = input("Enter The File Name:")
try:
    f = open(name)
except:
    f = open(name, "w")
    food = input("Enter item u had in meal: ")
    f.write(food)
    f.close()
else:
    print("File Is present")
    f = open(name, "r")
    print(f.read())
