'''
filter()
- makes list based on filter

'''

def greater_than_2(n):
    if n > 2:
        return True
    else:
        return False


l1 = [1,2,3,4,5,6,7,-2,-3,-4]
greater_than_2_list = list(filter(greater_than_2, l1))
print(greater_than_2_list)
