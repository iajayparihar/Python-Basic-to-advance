import pandas as pd
import numpy as np

dict={"Name" : ["ABhigyan","Venom","Vij","Mamta","Bangu"],
        "Age":[ 24, 12, 21 , 31 , 3],
        "Marks":[499,380,350,260,500]}
df=pd.DataFrame(dict)
print(df)
df.loc[1,"Age"]=np.NaN #must be same attributes "Age"
df.loc[2,"Name"]=np.NaN
df.to_csv("fivePersonInfo2.csv")
print("data written in a file successfully")