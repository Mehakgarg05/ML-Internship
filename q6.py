# Write a program that reads the content of a text file and prints it to the console

filename = "output.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
    
    print("The content of the file is:")
    print(content)

except Exception as e:
    print(f"An error occurred: {e}")
