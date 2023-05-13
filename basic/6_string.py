# immutable if u update it will give u typeerror
# a = "python"
# print(type(a))

# # To print string as it is
# str1 = """Hello
#         World, python"""
# print(str1)

# # Ways to defint string
# str5 = "python"
str2 = 'php'

# # Triple single quote
str3 = '''JavaScript'''

# str4 = """Java"""

# # Access string
# print(str3[2])
# print(str3[::-1])

# for x in str1:
#     print(x, end=" ")

# del str1
# print(str3)

# format printing
# name = "sudeep"
# age = 19
# rollNo = 32
# print("{},{},{}". format(name, age, rollNo))
# print(f"Name = {name}, Age = {age} and Roll No = {rollNo}")
# print(name + " Roll NO", rollNo, "Age", age)
# print("{1},{2},{0}". format("Abc", "xyz", "pqr"))


# Ennumerate=>Display character with indes number in list u can also store it inform of dict, tuple, set=>functionality same
# print(set(enumerate(str3)))

# Operators

# concat
# print(str2 + str3)
# # repeatasion *
# print(str3 * 2)

# # Membership
# print('J' in str3)

# # counting characters
# count = 0
# for x in str3:
#     if(x == 'a'):
#         count += 1
# print("count of J = ", count)

# string functions in python

str3 = "sudeep"
str2 = "Sawant"
print(str2.upper())
print(str2.capitalize())
print(str3.lower())

# spliting
str1 = "sudeepsawant@gmail.com"
# split after first
print(str1.split('first'))
list1 = list(str1.split('@'))
print(list1)

# two splited string will join using this content
# c = 'Email:'.join(list1)
# print(c)

# Find
print(str1.find(".com"))
# Replace
print(str1.replace("gmail.com", "outlook.com"))

# slicing
print(str1[2:])  # op: deepsawant@gmail.com

print(str1[4:16])  # op: epsawant@gma
