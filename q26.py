# Write a program in python that checks if a string starts with a given prefix 
# or ends with a given suffix

def check_prefix_suffix(input_string, prefix, suffix):
    starts_with = input_string.startswith(prefix)
    ends_with = input_string.endswith(suffix)
    
    return starts_with, ends_with

input_string = "Hello, World!"
prefix = "Hello"
suffix = "World!"
starts_with, ends_with = check_prefix_suffix(input_string, prefix, suffix)

print(f"String '{input_string}' starts with '{prefix}': {starts_with}")
print(f"String '{input_string}' ends with '{suffix}': {ends_with}")
