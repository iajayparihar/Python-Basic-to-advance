def myfun(**kwords):
	for key, value in kwords.items():
		print('%S==%S',(key,value))
#--main--
myfun(first="ajay",middle="parihar",last="001")