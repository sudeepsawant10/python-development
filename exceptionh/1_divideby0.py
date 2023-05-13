"""
try: => try block lets u test a block of a code for errors
except: => The block lets u to handel the errors
finally: => The block lets u execute code, reagardless of result of the try and except block
        This block always executes
else: =>if no exception execute this block

-if u handle the error your further code will execute.
"""

a = int(input("No1:"))
b = int(input("No2:"))

try:
    c = a/b
    print("c = ", c)
except ZeroDivisionError:
    print("You divided your no1 by zero!")
