# tell()=>Tells current position
# seek(offset [ , from])=>changes the current file pointer position


obj = open("D:\\python\\fileh\\read.txt", "r")
print("Current position: ", obj.tell())
print("Read string = ", obj.readline())
print("Letest current position: ", obj.tell())

# pos = obj.seek(0, 1) #go to current position
pos = obj.seek(0, 0)  # starting position 0
pos = obj.seek(0, 2)  # ending position 384
pos = obj.seek(2)  # starting position 2

print("Letest current position: ", obj.tell())
print("Now read string: ", obj.read())

obj.close()
