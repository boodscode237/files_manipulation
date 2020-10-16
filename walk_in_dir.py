import os
import shutil
# to give the filesnames and subfiles in a folder
for folderName, subfolders, filesnames in os.walk('path'):
    print('The folder is ' + folderName)
    print('The subfolder in ' + folderName + 'are: ' + str(subfolders))
    print('The filesnames in ' + folderName + 'are: ' + str(filesnames))
    print(type(str(subfolders)))

    # to delete a path containing a filename
    for subfolder in subfolders:
        if 'filename_to_delete' in subfolder:
            os.rmdir

    for file in filesnames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file),
                        os.join(folderName, file + '.backup'))
