Assignment 4 
==============

Program Description
===================

This project demonstrates basic **file handling operations in Python**.  
It consists of two main tasks: reading files with error handling, and writing/appending data to files.

---

## Task 1: Read a File and Handle Errors  
----------------------------------------

### Functionality

- Attempts to open and read the contents of a file.  
- If the file exists, its content is displayed.  
- If the file does not exist, an error message is shown instead.  
- This ensures the program does not crash when dealing with missing files.  

Example
-------
File content:

Hello Python class
Today we will learn Python
------------------------------------------
If file doesnot exist on same path

Error: The file 'sample.txt' was not found.



## Task 2: Write and Append Data to a File 
------------------------------------------- 

### Functionality

- Prompts the user to enter text, which is written into a file.  
- Allows the user to add more text that is appended to the same file.  
- Finally, the program displays the complete contents of the file after writing and appending.  
- This demonstrates how to create new files, overwrite existing ones, and add additional content safely.  

---
Example 
-------
Enter text to write to the file: GG 
Data successfully written
Enter additional text to append: BOIS
Data successfully appended

Final content of Output.txt:

GG
BOIS

## ▶️ How to Run  

1. Save the program in a `.py` file (e.g., `Assign_4__Task1.py`,`Assign_4__Task2.py`).  
2. Run the file using Python:  
   ```bash
   python Assign_4__Task1.py
   python Assign_4__Task2.py
