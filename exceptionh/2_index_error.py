
l = [1, 2, 3]
try:
    print("Result = ", l[2])
    print("Result = ", l[3])  # error in this line
except IndexError:
    print("You are accessing out of range value ")
