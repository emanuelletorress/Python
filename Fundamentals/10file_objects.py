
# ~~~~~~~~ reading a file

# in this way of reading a file, you have to explicitly close it
ff = open('text.txt', 'r')
print(ff.name)
ff.close()

# reading a file with context manager - automatically closes the file
with open('text.txt', 'r') as f:
    pass
    # .read() - returns the contents of the file
    # f_contents = f.read()

    # .readlines() - returns the contents of the file as a list, each line being an element in the list
    # f_contents = f.readlines()

    # .readline() - grabs the next line
    # f_contents = f.readline()
    # print(f_contents, end='') # it always ends with a new line so we're making it end with an empty string
    # f_contents = f.readline()
    # print(f_contents, end='')

    # there's a risk of running out of memory with .read(); so we can read the files like this
    """
    for line in f:
        print(line, end='')
    """

    # reading only a certain amount of characters on a file
    """
    f_contents = f.read(100)
    print(f_contents, end='')
    f_contents = f.read(100) # picks up where the previous one left off
    print(f_contents, end='')
    f_contents = f.read(100) # just prints an empty line since there are no more characters left
    print(f_contents, end='')
    """

    # reading only a certain amount of characters on a file through a loop
    """
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0: # while f_contents isn't an empty line
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
    """

    # f.tell() tells us where we are in the file
    """
    size_to_read = 100
    f_contents = f.read(size_to_read)
    print(f.tell())
    """

    # f.seek() puts us back at a certain point in the file
    
    """ size_to_read = 20
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f.seek(0)
    f_contents = f.read(size_to_read)
    print(f_contents, end='') """

# ~~~~~~~~ writing in a file

# if the file doesn't exists, this will go ahead and create it
# if the file does exist, this will overwrite it
with open('text2.txt', 'w') as f:
   pass
   """  f.write('Mary on a cross')
    f.seek(0)
    f.write('Misty Day') """

# for each line in rf, write that line in wf  
with open('text.txt', 'r') as rf:
    with open('text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# in order to read and write images, we use binary mode
""" with open('michael.jpg', 'rb') as rbf:
    with open('michael_copy.jpg', 'wb') as wbf:
        for line in rbf:
            wbf.write(line) """

# reading the image in chunks
with open('michael.jpg', 'rb') as rbf:
    with open('michael_copy.jpg', 'wb') as wbf:
        chunk_size = 4096
        rbf_chunk = rbf.read(chunk_size)
        while len(rbf_chunk) > 0:
            wbf.write(rbf_chunk)
            rbf_chunk = rbf.read(chunk_size)