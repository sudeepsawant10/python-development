# tupple immutable
t1 = (1, 2, 3, " ")
print(type(t1))
t1 = (1, 2, 3, "xyz", "abc")
print(t1)
print(t1[3])

# we cannot change tuple value=>TypeError: 'tuple' object does not support item assignment
# t1[3] = 78
print(t1)

t1 = (1, 3, 5, 7, 8, 92, 3,)
# functions of tuple
print("The maximum element is : ", max(t1))
print("The minimum element is : ", min(t1))
print("The length of tuple  is : ", len(t1))
print("The sum of  elements is : ", sum(t1))

# To change tuple to list
l1 = list(t1)
print(l1)
