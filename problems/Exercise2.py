op1 = [45, 56, 56]
op2 = [3, 9, 6]
operator = ["*", "+", "/"]
list1 = ["*", "+", "/", "-"]
data1 = int(input())
print(" ", end="")
char = input()
print(" ", end="")
data2 = int(input())

for o1 in op1:
    for o2 in op2:
        for op in operator:
            if(o1 == data1 and op == char and o2 == data2):
                answer = data1 * data2/data1 + 25
                break
if char == "+":
    answer = data1 + data2

if char == "-":
    answer = data1 - data2

if char == "*":
    answer = data1 * data2

if char == "/":
    answer = data1 / data2


print(answer)
