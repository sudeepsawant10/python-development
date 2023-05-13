#dictionary is mutable
# Consist of key : value pair

dict1 = {}
print(type(dict1))

dict1 = {
    "Name": "Rohan",
    "age": 2,
    18: "not completed",
    "hobbies": ["cricket", "painting"]
}

# print(dict1)
print("Name of the candidate is ", dict1["Name"])

#Update and insert
dict1["age"] = 17
print(dict1)

# to add new pair in dict
dict1.update({"DOB": '12/1/2004'})
print(dict1)

# To print the all keys of dict
print(dict1.keys())
# To print the all values of dict
print(dict1.values())

# To print all the content of dict we us .items()
print(dict1.items())

dict2 = {"name": "Jhone", "surname": "Doe"}
print(dict2)
# To clear the dict
dict2.clear()
print("Dictionary 2 Deleted : ", dict2)


# To copy dictionary into another dictionary
dict2 = dict1.copy()
print(dict2)

# To delte the dictionary
del(dict2)
# print(dict2) NameError: name 'dict2' is not defined

# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {"Harry": "Burger",
      "Rohan": "Fish",
      "SkillF": "Roti",
      "Shubham": {"B": "maggie", "L": "roti", "D": "Chicken"}}
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
print(d2)
del d2[420]
print(d2["Shubham"]["B"])
# d3 = d2.copy()
# del d3["Harry"]
# d2.update({"Leena":"Toffee"})
# print(d2.keys())
# print(d2.items())
