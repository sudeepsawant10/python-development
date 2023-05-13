# list comprehenstion
# list of numbers divisible by 3
ls = []
for i in range(100):
    if i % 3==0:
        ls.append(i)

# print(ls)
# same in one line of code
# add the data into list using this condition
ls2 = [i for i in range(100) if i%3==0]
# print(ls2)

# dict comprehension
# {0:"item0", 1:"item1".....}
# key:valeu
dict1 = {f"key{i}":f"value{i}" for i in range(100) if i%10==0}
# print(dict1)

# swapping key and value
dict_rev = {value:key for key, value in dict1.items()}
# print(dict_rev)

# list with unique values set
dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2"]}
# print(dresses)
# print(type(dresses))

#generator function => uses paranthesis
# eg. special type of iterators
evens = (i for i in range(101) if i%2 == 0) 
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(type(evens))


list_comp = [i for i in range(51) if i%5 == 0]
dict_comp = {f"key{i}":f"value{i}" for i in range(31)}
set_comp = {value for value in [1,2,3,4,1,2,3,4,2,3,1,4]}
# gen_comp = ()
print(list_comp)
print(dict_comp)
print(set_comp)
