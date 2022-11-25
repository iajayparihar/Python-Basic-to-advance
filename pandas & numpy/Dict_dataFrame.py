import pandas as pd
import numpy as np
dic={"student":["Ajay","Venom","Abhigyan"],"marks":[95,99,85],"sports":["crictek","football","chess"]}
frm=pd.DataFrame(dic)
print(frm)
print("__________________________________________")
ind=["I","II","III"]
frm=pd.DataFrame(dic,ind) 
print(frm)
