# open the file for writing
with open('writelines.txt', 'w') as f:
    # write a list of strings to the file
    # lst = ('Hello', ' ', 'Abhigyan')
    # lst = ['Hello', ' ', 'Abhigyan']
    # lst = 'hello my name is '
    f.writelines(lst)

with open('writelines.txt','r') as r :
    data = r.read()
    print(data)