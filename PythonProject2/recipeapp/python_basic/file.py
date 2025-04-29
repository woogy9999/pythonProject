import pandas as pd
import matplotlib.pyplot as plt
import csv
emp=pd.read_csv("c:\\pydata\\EMP.csv")
print(emp)
'''
result=emp.groupby("DEPTNO")['SAL'].mean().reset_index()
print(result)
result.plot.bar(x='DEPTNO',figsize=(8,5))
'''
result=emp.groupby("JOB")['SAL'].sum().reset_index
plt.show()