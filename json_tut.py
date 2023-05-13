import json

# json
data = '{"var1":"sudeep", "var2":20}'
data2 = "{'name':'sudeep', 'age':20, 'hobbies':['programming', 'gaming']}"

# string format
print(data)
print(data2)

# dict format
parsed = json.loads(data)
print(parsed)
# printing dict value
print(parsed['var1'])

dumped_data2 = json.dumps(data2)
paresd_data2 = json.loads(dumped_data2)
print(dumped_data2)
print(paresd_data2)

# data2 = {
#     "name":"sudeep",
#     "age":20,
#     "hobbies":["programming","gaming"],
# }
# sliced_data = data2.slice(2)
# print(sliced_data)
# js_json = json.dumps(data2)
# print(js_json)