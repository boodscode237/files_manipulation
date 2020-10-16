import os

print(os.path.exists('path'))
print(os.path.isfile('path'))
print(os.path.isdir('path'))
print(os.path.getsize('path'))
print(os.listdir('path'))

# Get the total size of a certain Document


def funcname(dirpath):
    total = 0
    for filename in os.listdir(dirpath):
        if not os.path.isfile(os.path.join('/Documents', filename)):
            continue
        total = total + os.path.getSize(dirpath, filename)
    return total


run = funcname('path')
print(run)
