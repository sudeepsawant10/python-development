# D:\\python\\fileh\\read.txt

# opening file with mode r+ =>read +write
# readline()=> reads the content line by line when we call it one by one.
fobj = open("D:\\python\\fileh\\read.txt", "r+")
print("Name: ", fobj.name)
# line = fobj.readline()
# # # One way to print file content
# print("Readline: %s" % (line))
# # # another way to print file content
# # print("Readline: ", line)

# # this will go to next line and read 7 charcters of file
# line = fobj.readline(7)
# print("Readline now : %s" % (line))

# if we do not store content in variable
# print("Line1: ", fobj.readline())
# print("Line2: ", fobj.readline())


# printing lines of file
line = fobj.readline()
print("1st line: %s" % (line))
line2 = fobj.readline()
print("2nd line: %s" % (line2))

fobj.close()
