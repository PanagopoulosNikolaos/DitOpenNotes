import os
import sys 


            
def create_new_files(folderPath,fileNum, name):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    
    
    for i in range(fileNum):
        newFile = name + f"_{i}.c"
        if os.path.exists(os.path.join(folderPath, newFile)):
            continue
        with open(os.path.join(folderPath, newFile), 'w') as f:
            pass
        


create_new_files(
    folderPath ="./Semester_2/C/String_LIB" ,
    name = "Lib_String_Exercise",
    fileNum = 20
)