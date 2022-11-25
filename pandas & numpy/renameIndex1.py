import pandas as pd
dict={"A":[9,8,7,5,2],
        'B':[7.4,1.2,4.4,8.8,5.5],
        'C':[90,91,92,93,94],
        'D':[1,2,3,4,5]}
mks1=pd.DataFrame(dict,index=(x for x in range(1,6)))
print(mks1)
print(mks1.rename(index={1:"I",2:"II",3:"III",4:"IV",5:"V"}))
print(mks1)

# parmanent save in data frame
mks1.rename(index={1:"I",2:"II",3:"III",4:"IV",5:"V"},inplace=True)
print(mks1)
print("---------------")
mks1.rename(columns={'A':'First','B':'Second'},inplace=True)
print(mks1)