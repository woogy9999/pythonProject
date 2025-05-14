import numpy as np
import pandas as pd
import oracledb as db
from pandas import DataFrame
import matplotlib.pyplot as plt

conn=db.connect("hr/happy@localhost:1521/XE")
cur=conn.cursor()
sql="SELECT * FROM emp"
cur.execute(sql)
emp=cur.fetchall()
cur.close()
conn.close()
print(emp)
column=['empno','ename','job','mgr','hiredate','sal','comm','deptno']
emp_df=DataFrame(emp,columns=column)
print(emp_df)
print(emp_df['ename'])
print(emp_df['sal'])

print(emp_df[['ename']][emp_df['ename'].apply(lambda x: x[1] == 'M')])
print(emp_df[['ename']][emp_df['ename'].apply(lambda x: x[0] == 'M')])
print(emp_df[['ename']][emp_df['ename'].apply(lambda x: x[-1] == 'E')])

names=emp_df['ename']
values=emp_df['sal']
plt.plot(names.values.tolist(),values.values.tolist())
plt.show()