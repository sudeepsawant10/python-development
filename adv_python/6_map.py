# Map function
# map(function_to_apply, list_of_inputs)
# performs operaiton on elements

h1 = [1,2,3,4,5,7]
sq = []

# normal way
for item in h1:
    sq.append(item**2)

print(sq)

def square(n):
    return n**2

# map way
sq = map(square, h1)
print(sq)
print(list(sq))