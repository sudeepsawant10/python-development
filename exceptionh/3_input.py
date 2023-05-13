# please keep code in try block that will have chances to throw the error
# try:
#     n = int(input("Enter number: "))
#     result = 10/n
# except ValueError:
#     print("Please enter number only!")
# except ZeroDivisionError:
#     print("we cannot divide by zero! pls enter another number...")

# ANOTHER WAY TO HANDLE INTEGER INPUT
try:
    n = int(input("No: "))
    result = 10/n
except (ValueError, ZeroDivisionError):
    print("Please give proper input!")
