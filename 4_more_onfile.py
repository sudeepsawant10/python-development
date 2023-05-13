f = open("sudeep")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())


# reset pointer
f.seek(0)
print(f.tell())
