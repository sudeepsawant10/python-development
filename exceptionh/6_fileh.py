# # giving error arguments
# try:
#     file = open("D://python//exceptionh//_file1.txt", "r+")
#     file.write("Python programming")
# except FileNotFoundError as f1:
#     print("File can't find! ", f1)
# except IOError as f2:
#     print("please check mode ", f2)
# else:
#     print("Successful")
#     file.close()
# finally:
#     print("Check file if successful")
#     print("else check path and mode of the file!")


# another way one line exception
""" VERY IMP DYNAMICALLY GIVING ERROR"""
try:
    file = open("D://python//exceptionh//_file1.txt", "r+")
    file.write("Python programming")

except (FileNotFoundError, IOError) as f:
    print("Please check the info->", f)

else:
    print("Successful")
    file.close()

finally:
    print("Check file if successful")
    print("else check path and mode of the file!")
"""
To print the inbuilt error msg
f1 = no such file or dir: _file.txt
f2 = not writable
"""
