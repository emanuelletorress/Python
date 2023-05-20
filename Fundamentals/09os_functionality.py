import os

# dir - all attributes and modules we have access while working with the os module
print(dir(os))

# current working directory
print(os.getcwd())

# changing the cwd
os.chdir('/Users/winte/Documents/Code/Python/')
print(os.getcwd())

# listing the files and folders in the current directory
print(os.listdir())

# creating/removing a new directory in the current directory
# os.mkdir('newDirectory')
# os.rmdir('newDirectory')

# creating/removing a directory with subdirectories
# os.makedirs('newDirectory/sub-dir-1')
# os.removedirs('newDirectory/sub-dir-1')

# renaming files and folders .rename('original-file-name', 'new-file-name')
# os.rename('text.txt', 'demo.text')

# ~~~~~~~ finding info about our files

# all info
# print(os.stat('demo.txt'))

# size of the file in bytes
# print(os.stat('demo.txt').st_size())

# last time the file was modified
# print(os.stat('demo.txt').st_mtime())

# last time the file was modified in readable form

# from datetime import datetime
# mod_time = os.stat('demo.txt').st_mtime()
# print(datetime.fromtimestamp(mod_time))

# shows dir/file tree within the desktop

for dirpath, dirnames, filenames in os.walk('/Users/winte/Desktop'):
    print('Current path: ', dirpath)
    print('Directories: ', dirnames)
    print('File names: ', filenames)
    print()