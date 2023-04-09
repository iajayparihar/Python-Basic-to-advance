# open the file for writing
with open('print.txt', 'w') as f:
    # write a string to the file using the print() function
    print('Hello, i m print method for write data in a file ', file=f)
