'''
reduce():
- To perform operation on whole list

'''
from functools import reduce

def sum_num(a, b):
    return a+b

li1 = reduce(sum_num, [1,2,3,4])
set1 = reduce(sum_num, (1,2,3))
print(li1)
print(set1)