import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
"""
    CSV 파일 읽기 / CSV 파일 추출
    JSON 파싱 / XML 파싱 방법
    파이썬 => 변수 (데이터 형 확인 => type)
             list / dict
             연산자 / 제어문 / 함수 / 예외 처리
             웹 = spring / spring-boot
"""
emp_df=pd.read_csv("c:\\pydata\\EMP.csv")
print(emp_df)
#create table empcp as select * from emp where dept=30
#empcp=emp_df[emp_df['DEPTNO']==30]
#print(empcp)
# emp_df=> select ename from emp
#print(emp_df['ENAME'])
#print(emp_df['JOB'])



data=emp_df[emp_df['DEPTNO'] == 20][['ENAME', 'JOB', 'SAL']].copy()
print(data)

# select empno,ename,job from emp where job='MANAGER';

data2=emp_df[emp_df['JOB']=='MANAGER'][['EMPNO','ENAME','JOB']].copy()
print(data2)

print(emp_df[['EMPNO','ENAME','JOB']][emp_df['JOB']=='MANAGER'])


names=emp_df[['ENAME']]
print(names)
sals=emp_df[['SAL']]
print(sals)

