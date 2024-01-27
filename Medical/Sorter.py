import math
import csv
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

specialtyList = []
yearsList = []

def average(list):
    sum = 0
    for val in list:
        if not math.isnan(val):
            sum+=val
    return float(sum)/len(list)

def add_field_name (df):
    specialty = ""
    for i in range(0, df.shape[0]):
        if isinstance(df["ACGME-Accredited Specialties"][i], str) and df["ACGME-Accredited Specialties"][i] =="":
            df["ACGME-Accredited Specialties"][i] = specialty
        elif pd.isna(df["ACGME-Accredited Specialties"].iloc[i]):
            df["ACGME-Accredited Specialties"][i] = specialty
        else:
            #print(df["ACGME-Accredited Specialties"][i])
            specialty = df["ACGME-Accredited Specialties"][i]
            if len(specialty) <50:
                specialtyList.append(specialty)
                #print(specialty,len(specialty))
    return df

import pandas as pd

csvList = []
for i in range(2017, 2023):
    currentY = i
    nextY = i + 1
    df = pd.read_csv(f"{currentY}-{nextY} Test.csv")
    #df = pd.concat([df.iloc[6:7], df.iloc[8:]], ignore_index=True)
    df = add_field_name(df)
    csvList.append(df)
    yearsList.append(currentY)
    df.to_csv(f'{currentY}-{nextY}.csv', index=False)  # Save to CSV without index

dict = {year: {specialty: [] for specialty in specialtyList} for year in yearsList}
#print(outer_dict)
for year in dict:
    df = csvList[year-2017]
    ind = 0
    #spec = specialtyList[ind] 
    spec = ""
    for i in range(0, df.shape[0]):
        if df["ACGME-Accredited Specialties"][i] != spec:
            ind+=1
        spec = df["ACGME-Accredited Specialties"][i] 
        print(year,i,spec,'-',df["Description of Test or Experience"][i],df["Average"][i])
        try:
            if df["Description of Test or Experience"][i] == "Number of work experiences":
                dict[year][spec] = df["Average"][i]
        except KeyError:
            pass

DF = pd.DataFrame(dict)
DF.to_csv('number of work experiences.csv')
