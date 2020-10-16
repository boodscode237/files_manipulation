import shutil
import os

shutil.copy('path_to_copy',
            'path_to_paste')

shutil.move('path_to_move',
            'path_to_paste')

os.getcwd()


# Deleting Files permanently(very dangerous)

os.chdir('path_to_delete')

for filename in os.listdir():
    if filename.endswith(('txt')):  # to delete the txt files
        os.unlink(filename)
        print(filename)
