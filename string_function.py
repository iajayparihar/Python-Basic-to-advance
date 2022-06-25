txt="i love apple,apple are my favorite fruits"
print("i love apple,apple are my favorite fruits")
x=txt.count("apple")
print('count("apple")=',x)

x=txt.count("apple",10,24)
print('count("apple",10,24) 10 to 24 location=',x)

x=txt.endswith("fruits")
print('endswith("fruits")=',x)

x=txt.endswith("are",10,24)
print('endswith("are",10,24)=',x)

print()
print()



txt="     banana       "
print("     banana       ")
x=txt.strip()
print('strip() for remove front and last whitespace=',x)

x=txt.lstrip()
print('lstrip() remove front whitespace=',x)

x=txt.rstrip()
print('rstrip() remove last whitespace=',x)

print()
print()

txt=",,,sssaaww.....banana"
print(",,,sssaaww.....banana")
x=txt.lstrip(",.asw")
print('lstrip(",.asw") use for start word scape=',x)

print()
print()

txt=",,,sssaBaww.....banana"
print(",,,sssaBaww.....banana")
x=txt.lstrip(",.asw")
print('lstrip(",.asw") use for start word scape but B is between them=',x)

print()

txt="I like bananas"
print("I like bananas")
x=txt.replace("bananas","apples")
print('replace("bananas","apples")=',x)

print()

txt="one one two three one "
print("one one two three one ")
x=txt.replace("one","four",2)
print('replace("one","four",2) = ',x)

print()
print()

txt="hello,welcome to my hell"
print("Hello,welcome to my hell")
x=txt.startswith("hello")
print('startswith("hello")',x)

x=txt.startswith("hello",7,20)
print('startswith("hello",7,20)',x)

print()
print()

txt="welcome to the jungle"
print("welcome to the jungle")
x=txt.split()
print('split()',x)

x=txt.split("e")
print('split("e")',x)

x=txt.find("to")
print('find("to")=',x)

x=txt.find("too")
print('find("too")=',x)

x=txt.find("to",4,10)
print('find("to",4,10)=',x)


x=txt.find("to",4,9)
print('find("to",4,9)=',x)


txt="Hello and welcome to my hell"
print("Hello and welcome to my hell")
x=txt.casefold()
print("txt.casefold",x)

print()
print()

txt="banana"
print("banana")
x=txt.center(20)
print("txt.center",x)

x=txt.center(20,"o")
print(x)


txt="for only {price:.2f} dollars!"
print(txt.format(price=65))

print("my name is {fname} , i am {age}.")
txt1="my name is {fname} , i am {age}".format(fname="ram",age=36)
print()
print(txt1)
print("my name is {0} , i am {1}")
txt2="my name is {0} , i am {1}".format("RAM",67)
print()
print(txt2)
print("my name is {} , i am {}")
txt3="my name is {} , i am {}".format("RaM",60)
print()
print(txt3)


txt='demo'
print("demo")
x=txt.isidentifier()
print(x)


txt="        "
x=txt.isspace()
print(x)

txt=('raj','anil','teena')
print("('raj','anil','teena')TUPLE",  x)
x="#".join(txt)


txt={"name":"ajay", "age":45,"markes":56}
print("('name':'ajay', 'age':45,'markes':56)",  x)
x="#".join(txt)
print(x)


txt="my name is Ajayyy"
print("my name is Ajayyy")
x=txt.swapcase()
print(x)

txt="50"
x=txt.zfill(10)
print(x)

txt="my name is ajayyy \n i am 23 years old"
x=txt.splitlines()
print(x)


txt="my name is ajayyy \n i am 23 years old"
x=txt.splitlines(True)
print(x)


txt="I eats banana all days"
x=txt.partition("banana")
print(x)











