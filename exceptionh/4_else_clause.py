# This is imp else block give u result if no errors occurs
try:
    n = int(input("Enter number: "))
    result = 100/n
except ValueError:
    print("Please enter number only!")
except ZeroDivisionError:
    print("we cannot divide by zero! pls enter another number...")
else:
    print("Division:", result)
