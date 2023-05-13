# w mode=>it will overwrite the existing content if previously written
# D:\\python\\fileh\\write.txt

# it will create or open file bcoz we are using w mode
obj = open("D:\\python\\fileh\\write.txt", "w")
# obj.write("This is 1st line written using writefile.py")
obj.write("This is 2nd line written using writefile.py")  # overwritten
obj.close()

# you can also use with keyword to write the file
