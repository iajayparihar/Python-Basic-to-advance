import pandas as pd
ontutd={'tutor':["Tahira","ajay","vij","Mamta",
                "Tahira","ajay","vij","Mamta",
                "Tahira","ajay","vij","Mamta"],
        'classes':[12,16,13,15,
                    17,35,15,24,
                    45,75,84,92],
        'Quater':[1,1,1,1,
                    2,2,2,2,
                    3,3,3,3],
        "Country":["Indore","Indore","Banglour","Indore",
                    "Indore","Hydrabad","Banglour","Hydrabad",
                    "Hydrabad","Indore","Indore","Hydrabad"]
        }
df1=pd.DataFrame(ontutd)
print(df1)
print("--------------")
pivt=df1.pivot_table(index='tutor',columns='Quater',values='classes').fillna(0)
print(pivt)
print("--------------")

pivt=df1.pivot_table(index='tutor',values='classes',aggfunc='sum').fillna(0)
print(pivt)

print("--------------")
pivt=df1.pivot_table(index=['tutor','Country'],values='classes',aggfunc='sum').fillna(0)
print(pivt)

df1.sort_values("Country",inplace=True,ascending=False)
print(df1)

df1.sort_values(["Country","tutor","Quater"],inplace=True,ascending=False)
print(df1)
