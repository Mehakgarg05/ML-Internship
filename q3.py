# 3. Write a python program that calculates the factorial of a given number.

num = int(input("enter number: "))
product = 1
for i in range(1,num+1):
    product = product*i

print("Factorial of given number is: ", product)
