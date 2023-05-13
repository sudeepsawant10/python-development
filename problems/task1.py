"""# path of this script 
directory = "C:\\Users\\Sudeep\\Desktop\\py\\"
filepath = directory + input("Enter filename: ")
"""

# Creates a new file
fname=input("Enter the file name: ")
try:
    f = open(fname)
except:
    f = open(fname, 'w')
    phy=int(input("Enter physics marks: "))
    chem=int(input("Enter chemestry marks: "))
    maths=int(input("Enter maths marks: "))
    bio=int(input("Enter biology marks: "))
    cs=int(input("Enter computer science marks: "))
    f.write("pysics = {} \nchemistry = {}\nMaths = {}\nBiology = {}\nComputer Science = {}\n".format(phy,chem,maths,bio,cs))
    total =phy+chem+maths+bio+cs
    percentage = (total / 500.0) * 100
    f.write("Percentage = {}".format(percentage))
    f.close();
else:
    f = open(fname, 'r')
    print(f.read())
'''
name=input("Enter The File Name:")
try:
    f=open(name)
except:
    f=open(name,"w")
    print("Enter The Marks Of 5 Subjects:")
    phy = input("Enter The Marks Of Physics:")
    che = input("Enter The Marks Of Chemistry:")
    maths = input("Enter The Marks Of Maths:")
    bio = input("Enter The Marks Of Biology:")
    cs = input("Enter The Marks Of Cs:")
    total = int(phy)+int(che)+int(maths)+int(bio)+int(cs);
    p = int(total)*100
    per = p/500
    total = str(total)
    per = str(per)
    f.write("MARKS Of Physics:")
    f.write(phy)
    f.write("\n")
    f.write("MARKS Of Chemistry:")
    f.write(che)
    f.write("\n")
    f.write("MARKS Of Maths:")
    f.write(maths)
    f.write("\n")
    f.write("MARKS Of Biology:")
    f.write(bio)
    f.write("\n")
    f.write("MARKS Of CS:")
    f.write(cs)
    f.write("\n")
    f.write("Total Score is :")
    f.write(total)
    f.write("\n")
    f.write("percentage is :")
    f.write(per)
    f.write("%")
    f.write("\n")
    f.close()
else:
    print("File Is present")
    f=open(name,"r")
    print(f.read())
'''
