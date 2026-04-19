# *********************With sintex ***********************
""" with open("new.txt","r") as f:
    print(f.read())

with open("new.txt","w") as f:
    f.write("Hello World") """

# *********************Deleting a file ***********************

import os    
os.remove("new.txt")  # This will delete the file
print("File Deleted")  # This will print the message after deleting the file