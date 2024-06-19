# Write a program that takes a string input from the user and writes it 

text = input("Please enter a string to be written to a text file: ")

filename = "output.txt"

# Open the file in write mode and write the user's input
with open(filename, "w") as file:
    file.write(text)

print("The string has been written.")
