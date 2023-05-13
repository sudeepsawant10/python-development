# finally => always executed

try:
    n = int(input("Enter number: "))
    result = 10/n
except ValueError:
    print("Please enter number only!")
except ZeroDivisionError:
    print("we cannot divide by zero! pls enter another number...")
else:
    print("Result = ", result)
finally:
    # if error occures this line says: NameError: name 'result' is not defined else work well
    # print("Result = ", result)
    print("Thank u for your response :)")
