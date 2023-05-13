import json
   
   
with open("D:\\python\\data.json") as file:
    # data = file.read()
    parsed = json.load(file)
    print(parsed)

    # for val in parsed['schemeName']:
    #     print(val)