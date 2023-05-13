# print hello , world 5 times

# for i in range(1, 6):
#     print("Hello, World")

# using while loop
# i = 1
# while(i <= 5):
#     print("hello, World")
#     i += 1

# factorial of number
# n = int(input("Enter the number: "))
# fact = 1
# i = 1
# while(i <= n):
#     fact = fact * i
#     i += 1
# print("Factirial of ", n, " is ", fact)

# # printing using f stream
# print(f"Factorial of {n}, is {fact}")

# program 4 armstrong number
# 153 = 1*1*1 + 5*5*5 + 3*3*3 =>153

n = int(input("Enter the number: "))

# Converting int into str coz we cannot find length of integer
len = len(str(n))
r = 0
a = n
while(n > 0):
    mod = n % 10
    n = n//10
    r = r+mod**len

if(a == r):
    print("The no. is armstrong")
else:
    print("Not an armstrong!")
