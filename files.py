import os

print(os.path.exists('/home/abodo/Documents/file_manipulation/file.py'))
print(os.path.isfile('/home/abodo/Documents/file_manipulation/LICENSE'))
print(os.path.isdir('/home/abodo/Documents/file_manipulation'))
print(os.path.getsize('/home/abodo/Documents/file_manipulation/LICENSE'))
print(os.listdir('/home/abodo/Documents/'))

# Get the total size of a certain Document


def funcname(dirpath):
    total = 0
    for filename in os.listdir(dirpath):
        if not os.path.isfile(os.path.join('/Documents', filename)):
            continue
        total = total + os.path.getSize(dirpath, filename)
    return total


run = funcname('/home/abodo/Documents')
print(run)
