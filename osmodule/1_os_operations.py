
import os

# get current working directory
print("current dir: ", os.getcwd())

# changed directory
print("Changed dir: ", os.chdir("D://python"))
print("current dir: ", os.getcwd())

# Make directory (create)
# os.mkdir("created")    #create only once if not will give u fileexists error

# create dir 'aa' in this locaion
# os.mkdir("D://python//gui//aa")

# Rename dir
# os.rename("created", "test")
