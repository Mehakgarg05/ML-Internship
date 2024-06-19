# Write a program in python that counts the frequency of each character in 
# a string

str = input("Enter a string:")
lst = str.split("")
for i in range (0, len(lst)):
    character = lst[i]

    print("count of character", character, lst.count(character))

