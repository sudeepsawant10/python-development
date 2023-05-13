"""
a=list()
print(a)
list1 = [1,2,"xyz",34.56]
print(list1)
#access list element using index
print(list1[2])

#update list 2nd element
list1[1] =8
print(list1)

#add new element into list using append
list1.append(9)
print(list1)

#add elment at specific position
list1.insert(2,"abc")
print(list1)

#Remove element
list1.remove("xyz")
print(list1)
list1.remove("abc")
#sort the elements
list1.sort()
print(list1)

#list functions
l = [3,5,8,6,10,12,24,15]
print(l)

#Max number in list.
print(max(l))

#len of list.
print(len(l))

#convert list to tuple
l2 = tuple(l)
print(l2)

#delete list
#del(list1)
print(list1)

#extend list1 with list2
list1=[1,2,3]
list2=[1.1,1.2,1.3]
list1.extend(list2)

list1=[1,2,3]
#if we try to append in list1
list1.append(list2)
print(list1)

#empty list
list1.clear()
print(list1)

"""
"""
#other important functions of list
list1=[134,3,1,2,45,45,1,2,3,1]
list1.sort()
print(list1)

#Reverse the list
list1.reverse()

#count the list element in list
print(list1.count(1))

print(list1)
#Remove the element 
list1.remove(2)
print(list1)

#Remove the element using index
list1.pop(2)
print(list1)

#poping using negative index
list1.pop(-7)
print(list1)

"""

"""
#slicing the list using indexing
list1=[134,45,3,2,1,1,1,1,1,1,]
print(list1)

print(list1[2:])

#from - upto 
print(list1[2:6])

#starting to 3rd indexing
print(list1[:3])

#only 1 element
print(list1[9:10])

#Negative indexing printing from last to first
print(list1[::-1])

#starting to end upto -3rd index position
print(list1[:-3])
"""

#operators in list
list1=[1,2,3,4]
list2=[5,6,7,8]

#addition => adding other elements into list
list3 = list1 + list2
print(list3)
#multiplying the elements of the list (n times adding) 
list3 = list1 * 2 + list2 * 2
print(list3)
print(list2*4)

#finding the element in list
print(8 in list1)
print(8 in list2)
