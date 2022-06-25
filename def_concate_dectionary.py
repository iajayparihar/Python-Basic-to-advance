def diccon(xdic,ydic):
	dicz ={**xdic,**ydic}
	return dicz
#--main--
dic1={1:"Ajay",2:"abhigyan"}
dic2={3:"yatin",4:"deep"}
maindic=diccon(dic1,dic2)
print(maindic)