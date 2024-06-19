# Write a python program that takes a list of numbers and returns their sum

num = input("Enter few numbers")
numbers = num.split()
numbers = [int(i) for i in numbers]
sum =0
for i in numbers :
    sum+= i

print("sum of numbers is :", sum)