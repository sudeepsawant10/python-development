# we can use range() function in for loop
# range(5)= 0,1,2,3,4
# range(2,6)= 2,3,4,5

# print from 1 to 20
# for x in range(1, 21):
#     print(x)

# printing including last element using range()
n = int(input("Number: "))
for s in range(1, n+1):
    print(s)

# program 01 : jumping in loop
# 2 = jump
# for every 2nd element jump skip it
# for x in range(1, 16, 2):
#     print(x)

# program 02 : Reverse printing
# n = int(input("Number: "))

# # third argument -2 is for jump
# for x in range(n, 0, -2):
#     print(x)

# program 03: iterating the list
# list1 = [1, 2, 3, 4, 5, 6, 7]
# for x in list1:
#     print(x)

# program : 04 Reverse no
# n = int(input("Number: "))
# temp = n
# while(div != 0):
#     mod = temp % 10
#     rev = div*10 + mod
#     temp = temp/10


# program : 05 String
str = "python coding"
for x in str:
    print(x, end=" ")

    list1 = [
        ["kiran", 8],
        ["Akash", 4],
        ["duru", 15],
        ["shubham", 9],
        ["varun", 8],
    ]
# for item, bdate in list1:
#     print(item, "Birthdate is ", bdate)

# # converting list1 to dict and iteraing it
# dict1 = dict(list1)
# print(dict1)
# # if u don't give items() function it will give u error becoaz it is dictionary
# for item, bdate in dict1.items():
# print(item+"'s Birthdate is ", bdate)

# if u want only key then do this
# for item in dict1:
#     print(item)
items = [int, float, "sudeep", 5, 8, 9, 4, 3, 45]
for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)
