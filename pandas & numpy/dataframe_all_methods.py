import pandas as pd 
dict={'population':[126877,56458,12345,22224],
        'Hospital':[1555,333,451,1111],
        'School':[10,20,30,40]}
dtf1=pd.DataFrame(dict,index=['delhi','mumbai','kolkata','channi'])
print("------------------1")
print(dtf1)
print("------------------2")
# print( dtf1.loc['delhi']) # key index 
# print("------------------")
print("Delhi row :- ")
print(dtf1.loc['delhi',:]) 
# delhi column value
print("------------------3")
print(dtf1.loc['mumbai':'channi',:]) # row index  mumbai to chenni
print("------------------4")
print(dtf1.loc[['mumbai','channi'],:]) # row index mumbai and chenni
print("------------------5")
print(dtf1.loc[:,'Hospital'])
print("------------------6")
print(dtf1.loc[:,'population':"Hospital"]) #please maintain column order
print("------------------7")
print(dtf1.loc[["mumbai","channi"],:"Hospital"])
print("------------------8")
print(dtf1.loc["mumbai":"channi","population":"Hospital"])
print("------------------9")
print(dtf1.loc[['mumbai','channi'],['population','School']])
print("------------------10")
print(dtf1.loc['delhi':'channi',['population','School']])
print("------------------11")
print(dtf1[1:3]) # task perform in key index
print("------------------12")
print(dtf1.iloc[1:3])
print("------------------13")
print(dtf1.iloc[1:3,0:2])
print("------------------14")
print(dtf1.population['mumbai'] ) # in a mumbai key , value at population 
print("------------------15")
print(dtf1.population[1] ) 
print("------------------16")
                # key index    column index
print(dtf1.at['mumbai','population'] ) 

print("------------------17")
print(dtf1.iat[1,0] ) 
