#  1. Create and Write to a File
filename = "sample.txt"

file = open(filename, "w")
file.write("Welcome to Python File Handling\n")
file.write("This file is created using Python.\n")
file.close()

print("File created and written successfully.\n")

#  2. Read the File
file = open(filename, "r")

print("Reading file content:")
content = file.read()
print(content)

file.close()

# 3. Append More Data to the File
file = open(filename, "a")

file.write("This line is added using append mode.\n")
file.close()

print("New content appended.\n")

# 4. Read Again to Show Updated Content
file = open(filename, "r")

print("Updated file content:")
print(file.read())

file.close()

#  5. Delete the File
import os

if os.path.exists(filename):
    os.remove(filename)
    print("\nFile deleted successfully.")
else:
    print("\nFile not found.")