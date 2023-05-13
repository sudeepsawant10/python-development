obj = open("D:\\python\\fileh\\appendplus.txt", "a+")
print("present content: ")
obj.seek(0)
print(obj.read())  # content in file => existing line 1 use seek to read
obj.write("This is 2nd line appended using a+ mode")
print("Updated content")
obj.seek(0)
print(obj.read())
obj.close()

# if u want previous content and also for reading use a+ mode
"""
In a+ mode:
-u can read the content initially using seek and read methods
-The previous content will remain as it is event if write additional content into the file so append method is useful to keep previous content also in the file
"""
