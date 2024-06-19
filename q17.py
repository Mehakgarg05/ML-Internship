# Write a program in python that converts a given string to title case (first 
# letter of each word capitalized)

input_string = input("Enter a string: ")
words = input_string.split()

title_case_string = ' '.join([word.capitalize() for word in words])

print("Original string:", input_string)
print("Title case string:", title_case_string)
