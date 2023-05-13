'''
1. Iterable
- __getitem__ is defined
- it can give iterator
2. Iterator
- next method is defined

3. Iteration
- can traverse to next element using iterator

Generators:
- It is iterator which can be use at once.
- for large dataset
'''

def gen(n):
    for i in range(n):
        # 
        yield i

# created an object 
# we can save system's ram
print(gen(10000000))
# for i in gen(10000):
#     print(i)

name = "harry"
iter1 = iter(name)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
