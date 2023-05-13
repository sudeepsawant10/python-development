
# for r+ mode file must be exists to read file
# It will over write existing content if write anything to it
obj = open("D:\\python\\fileh\\readplus.txt", "r+")
# print(obj.read())  # content in file => existing line 1
obj.write("This is 5th line written using r+ mode")
obj.seek(0)
print(obj.read())
# it will not work bcoz file pointer changed previously for that use=>obj.seek(0)print(obj.read())
obj.close()
# obj.wrtie() => function writtens the character written into the file
"""
Note:
when u read some content previously from file and then after u write so the previous content will not be overwritten 
because the writing to file start in the position where previous read ends
-and it also don't need to use seek(0) method initially it direactly reads the file
-if u read the file initally it will keep the content bcoz cursor changes according to reaad
-but if u don't the content will overwrite.
- if u write initally it will keep further data as it is.
"""
