
class demo(Exception):
    pass


num = int(input("No: "))

try:
    if num != 10:
        raise demo
except demo:
    print("Value entered is not correct")
else:
    print("Correct Value ", num)
