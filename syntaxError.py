try:
    print('hello')
    print(eval('my name is john'))
except SyntaxError as e:
    print('error:-',e.filename)
    print('error:-',e.lineno)
    print('error:-',e.offset)
    print('error:-',e.text)
    print('error:-',e)