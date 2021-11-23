import pandas as pd 
import os
from pandas.core.frame import DataFrame

PATH="" # Enter path here
outputfile="" #Enter csv filename here like: output.csv
filelist=[]

for filename in os.listdir(PATH):
    if filename.endswith(".csv"):
         filelist.append(os.path.join(PATH+"\\",filename))
    else:
        continue

df = pd.concat(
    map(pd.read_csv, filelist), ignore_index=True)

df.to_csv(os.path.join(PATH+"\\",outputfile),index=False)