import pandas as pd
from sqlalchemy import create_engine
import pymysql

engine= create_engine('mysql+pymysql://root:Abhigyan786@localhost/employee')
mycon = engine.connect()

print("cnnection successfull")