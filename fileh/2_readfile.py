# read file using read mode

fobj = open("D:\\python\\fileh\\read.txt", "r")

# read the 12 characers and print
# if file not exist it will give u filenotfound error so we have to create it

# print(fobj.read(12))
print(fobj.read())
fobj.close()
