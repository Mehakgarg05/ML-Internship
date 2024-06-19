def read_lines():
    lines = []
    print("Enter multiple lines of text:")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    return lines

def main():
    # Read lines from the user
    lines = read_lines()
    
    # Print the lines
    print("\nYou entered:")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
