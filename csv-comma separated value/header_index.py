import pandas as pd
dict={"Name" : ["ABhigyan","Venom","Vij","Mamta","Bangu"],
        "Age":[ 24, 12, 21 , 31 , 3],
        "Marks":[499,380,350,260,500]}
df=pd.DataFrame(dict)
print(df)
df.to_csv("fivePersonInfo1.csv",header=None,index=False)
print("data written in a file successfully")