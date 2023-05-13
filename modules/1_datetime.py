"""
datetime.now() => current date and time
datetime.today() => current date

classes of datetime module
1. date class
2. time class
3. datetime class
"""

# program 1 datetime
# import datetime
# d = datetime.date(2021, 5, 29)
# print("Todays date = ", d)

# program 2 time
# from datetime import time
# a = time()
# print(a)

# b = time(11, 34, 55)
# print(b)

import time
initial = time.time()
# print(initial)
# k = 0
# while(k < 50):
#     print("This is print 1")
#     k += 1
# print("While loop ran in ", time.time() - initial, "Seconds")

# initial2 = time.time()
# for i in range(50):
#     print("This is print2 in for")

# print("While loop ran in ", time.time() - initial2, "Seconds")
