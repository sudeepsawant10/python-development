'''
lambda:
- syntax:
lambda argument:manipulate(argument)
anonomyous function (inline defination)
Use
- easy syntax 

'''

# def add(a, b):
#     return a+b

add = lambda x,y: x+y
print(add)
mul = lambda a,b: a*b
print(add(4,6))
print(mul(4,6))

l1 = [(8,1), (555, 34), (9,5),]
l2 = [6,4,7,3,1,9]
print(l2)
l2.sort()
print(l2)

print(l1)
l1.sort(key = lambda x:x[1])
print(l1)

