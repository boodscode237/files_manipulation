import shutil
import os

shutil.copy('/home/abodo/Documents/hello.txt',
            '/home/abodo/Documents/file_manipulation/copied_to_this_folder.txt')

shutil.move('/home/abodo/Documents/file_manipulation/copied_to_this_folder.txt',
            '/home/abodo/Documents/hello.txt')

os.getcwd()


# Deleting Files permanently(very dangerous)

os.chdir('path_to_delete')

for filename in os.listdir():
    if filename.endswith(('txt')):  # to delete the txt files
        os.unlink(filename)
        print(filename)
