#Marks and percentage
"""
name = input("Name: ")
n = int(input("No. of subjects: "))
marks = []
for x in range(1, n+1):
    a = int(input("marks: "))
    marks.append(a)

print("Name: ", name)
print("Marks obtained: ", sum(marks))
print("Percentage: ", sum(marks)/n)
"""

# Q.1. List comphrension
# s = [x**2 for x in range(1, 51)]
# print(s)

# s = [x**2 for x in range(1, 51) if (x**2 % 5 == 0)]
# print(s)

# s = []
# for x in range(1, 26):
#     s.append(x**2)
# print(s)

# Q.2.  convert dict into two lists
dict1 = {
    1: "xyz",
    2: "Abc",
    3: "Pqr"
}

list1 = []
list2 = []

# append keys of dict1 into list1
# for x in dict1.keys():
#     list1.append(x)

# # append values of dict1 into list2
# for x in dict1.values():
#     list2.append(x)

# ANOTHER METHOD TO ADD DICT KEY AND VALUES INTO KEY LIST AND VALUES LIST

# for k, v in dict1.items():
#     list1.append(k)
#     list2.append(v)
# print(dict1)
# print(list1)
# print(list2)

# # CONVERT Two LISTs TO DICTIONARY
# dict2 = {}

# for x in range(0, len(list1)):
#     dict2.update({list1[x]: list2[x]})
#     # it is similar to insert key value in dict
#     # dict2.update({"name": "sudeep"})

# dict2.update({"name": "sudeep", "Roll": 32})
# print(dict2)

list4 = ["sudeep", "kiran", "akash", "rohit"]
name = input("Enter name: ")

if name in list4:
    x = list4.index(name)  # return the index of element
    print(list4[x])  # print list element of that index

print(list4[2])
