# Write a python program that calculates the sum of the digits of a given 
# number

num = int(input("Enter a number:"))
sum =0
while(num>0):
    sum = sum +(num%10)
    num = int(num/10)

print(sum)