# Write a python program that checks if a substring is present in a given
# string.

string = input("Enter main string :")
substring = input("Enter substring :")
if substring in string:
    print("Substring is present in the given string")
else:
    print("Substring is not present")