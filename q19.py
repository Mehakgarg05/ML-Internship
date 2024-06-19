# 19. Write a python program that removes all punctuation from a given string.
import string
def remove_punctuation(input_string):
    punctuation = string.punctuation
    
    cleaned_string = ""
    for char in input_string:
        if char not in punctuation:
            cleaned_string += char
    
    return cleaned_string

str = "Hello, world! "

# Remove punctuation from the input string
cleaned_string = remove_punctuation(str)
print("Cleaned string:", cleaned_string)
