import os

def createNewFiles(folder_path: str, file_num: int, name: str):
    """
    Creates multiple empty C source files in a specified directory.
    
    Checks if the directory exists and creates it if not. Skips existing files
     to prevent overwriting content.

    Args:
        folder_path (str): The destination directory for the new files.
        file_num (int): The quantity of files to generate.
        name (str): The prefix string for the filenames.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Ensures path existence before file operations.
    
    for i in range(file_num):
        new_file = f"{name}_{i}.c"
        full_path = os.path.join(folder_path, new_file)
        
        if os.path.exists(full_path):
            continue  # Avoids destructive overwrites of existing student work.
            
        with open(full_path, 'w') as f:
            pass  # Initializes an empty template file.

if __name__ == "__main__":
    # Example usage for the C Programming II course module.
    createNewFiles(
        folder_path="./Year_1/Semester_2/C_PROGRAMMING_II/Examples/String_LIB",
        name="Lib_String_Exercise",
        file_num=20
    )
