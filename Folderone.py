#Setting up a system to recover -x- prefixed files and inserting them into a specific folder.
#Importing the main libraries

import os
import shutil 

dirList = os.listdir() # A list of all files in the current directory 


prefix = input('Insert a prefix: ') 
newFolderName = str(prefix) + 'world'
os.mkdir(newFolderName)

# Creation of a new folder and relocation 

for file in dirList:
    if str(file).startswith(prefix):
        shutil.move(file, newFolderName)

    input('Press any key to terminate' )
    


