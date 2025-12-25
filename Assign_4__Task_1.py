# Assignment 4  # Task 1

# ReAD A File  and Handle Error

def read_file(filename):
    try:
        # Try opening the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except FileNotFoundError:
        # Handle case when file does not exist
        print(f"Error: The file '{filename}' was not found.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

# Calling Function
msg = "Read File content \n"
read_file("sample.txt")
