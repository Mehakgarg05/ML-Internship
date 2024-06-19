# Write a program that copies the contents of one text file to another


source_file = 'source.txt' 
destination_file = 'destination.txt'  

try:
    with open(source_file, 'r') as source:
        content = source.read()
        with open(destination_file, 'w') as destination:
            destination.write(content)
    
    print(f"Successfully copied content from '{source_file}' to '{destination_file}'.")

except Exception as e:
    print(f"An error occurred: {e}")
