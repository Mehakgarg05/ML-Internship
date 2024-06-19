# Write a python program that checks if two strings are anagrams of each 
# other

str1 = input("enter string 1 ")
str2 = input("enter string 2 ")

arr1 = sorted(list(str1))
arr2 = sorted(list(str2))

if(arr1 == arr2):
    print("given string are anagrams")

else:
    print("Given string are not anagrams")

