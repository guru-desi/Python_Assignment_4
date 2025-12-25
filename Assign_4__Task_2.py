# Assignment 4  # Task 2

# Write and Append Data to a file 

def writ_file(filename):
    # Open file in write mode first (creates/overwrites)
    with open(filename, 'w') as file:
        file.write(input("Enter text to write to the file: "))
        print("Data successfully written")

    # Open file in append mode (adds new content at the end)
    with open(filename, 'a') as file:
        file.write("\n" + input("Enter additional text to append: "))
        print("Data successfully appended")

    # Finally, open file in read mode to display contents
    with open(filename, 'r') as file:
        print("\nFinal content of Output.txt:\n")
        print(file.read())

# Call the function
writ_file("Output.txt")
