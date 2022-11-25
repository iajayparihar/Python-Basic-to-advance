import pandas as pd
dict={'A':[1,5,8] ,"B":[9,4,5],"C":[4,3,2]}
obj=pd.DataFrame(dict)
print(obj)

print(obj>5)
print(obj[obj['B']>4])                                 