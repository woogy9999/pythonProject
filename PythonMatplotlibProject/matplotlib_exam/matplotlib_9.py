import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

file=open('c://pydata//seoul.csv','r',encoding='utf-8')
data=csv.reader(file)
header=next(data)
#print(data)
max_temp=-999
max_date=''
#print(header)
for row in data:
    if row[-1]=='':
        row[-1]=-999
    row[-1]=float(row[-1])
    if max_temp<row[-1]:
        max_date=row[0]
        max_temp=row[-1]
    print(row)
print(f"가장 기온 높은 날 : {max_date}")
print(f"온도 : {max_temp}")
file.close()