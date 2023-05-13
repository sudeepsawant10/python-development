with open("D:\\python\\fileh\\read.txt", "w+") as obj:
    obj.seek(42)
    print("Contetn = ", obj.read(13))
    print("Current postion = ", obj.tell())

    obj.seek(42)
    obj.write("2_writfile.py")
    obj.seek(0)
    content = obj.read()
    print(content)
