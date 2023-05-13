s = set()
print(type(s))

l = [1, 2, 3, 4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))

# set stores unique value
s.add(1)
s.add(1)
s.add(2)
s.add(2)
s.add(3)

# It will make new set
s1 = s.union({1, 2, 3, 4, 5})
print(s, s1)

# Intersection common
s1 = s.intersection({1, 2, 3, 4, 5})
print(s, s1)

# disjoint
s1 = {4, 6}
print(s.isdisjoint(s1))

# remove element
s.remove(2)
print(s)
