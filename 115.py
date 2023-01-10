import os
 
source="main.txt"
dest="newmain.txt"

os.rename(source,dest)
print("Source path renamed to destination path successfully!")