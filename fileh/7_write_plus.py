# w+ => write plus write and cannot append so read function will not work here
obj = open("D:\\python\\fileh\\writeplus.txt", "w+")
print("Present Content")
obj.seek(0)
print(obj.read())  # not woking
obj.write("This is 2nd line overwritten using w+ mode")
print("After written: ")
obj.seek(0)
print(obj.read())  # not woking
obj.close()
"""
In w+ mode:
it will read the content using seek and read only after u write to it 
-if u try to read the content initialy it will not work
"""
