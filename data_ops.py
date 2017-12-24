import data_loading

data=data_loading.get_data_json('https://data.gov.in/node/1895961/datastore/export/json')

import pandas as pd
import numpy as np


col_map={}
col_list=[]
Killed_cols=[]

def make_col_map_list():
    index=0
    for i in data['fields']:
        col_list.append(i['label'])
        col_map[i['label']]=index
        index+=1
    # print (col_map)
    # print (col_list)
    for i in col_list:
        if "Killed" in i:
            Killed_cols.append(i)
    # print (Killed_cols)

def removeNA(x):
    if x=='NA':
        # print (x)
        return int(0)
    else:
        return x
def make_data_frame():
    make_col_map_list()
    # print (type(data['data']))
    df=pd.DataFrame(data['data'],columns=col_list)
    # print (df.describe())
    print (df.iloc[:,0].tolist())
    df=df.applymap(removeNA)
    return df
    # print (df.head())

