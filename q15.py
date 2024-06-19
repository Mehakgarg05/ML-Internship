# Write a program that reads data from a CSV file and prints it to the 
# console.

import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(', '.join(row))

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the path : ")
    
    read_csv(file_path)

if __name__ == "__main__":
    main()
