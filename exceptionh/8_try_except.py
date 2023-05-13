try:
    # print("I will try this code and will throw exception if thery is any problem")
    open("text.txt")
except Exception as e:
    print("I will run only if try block fails")
# if exception doesn't occur the else part will run
else:
    print("I will run only if there is no exception. Use this to run code which should only execute if there is no exception")
finally:
    print("this willl be printed in every case")