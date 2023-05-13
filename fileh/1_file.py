# create or open file on this locaion
fo = open("C:\\Users\\Sudeep\\OneDrive\\Desktop\\python\\fileh\\foo.txt", "w")
print("Name of the file = ", fo.name)
print("if file is closed? : ", fo.closed)
print("Mode of the file : ", fo.mode)
fo.close()
