dic1={'ten':10,'twenty':20}
dic2={'thirty':30,'fourty':40}
dic3={**dic1,**dic2}  # concate dic1 and dic2 and contain { key : value } in dic3 with dictionary formate
print(type(dic3))
print(dic3)
dic3={*dic1,*dic2} # concate dic1 and dic2 and contain ' keys ' in dic3 with set formate
print(type(dic3))
print(dic3)