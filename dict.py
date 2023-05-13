context = {
    "iphone":{"model":"iphone 11", "selling_price": 80000, "discount_price": 75000},
    "redmi":{"model":"redmi note 11", "selling_price": 50000, "discount_price": 45000}
}
print(context)
print(context["iphone"])
print(context["iphone"]["model"])
print("printing model")
for p in context:
    print(context[p])