import numpy as np
import pandas as pd
import oracledb as db
import matplotlib.pyplot as plt

#C:\springDev\springStudy\.metadata\.plugins\org.eclipse.wst.server.core\tmp0\wtpwebapps\SpringLastProject\
def empGraphData():

    conn=db.connect("hr/happy@localhost:1521/XE")
    cur=conn.cursor()
    sql=f"""
            SELECT empno,ename,job,TO_CHAR(hiredate,'YYYY-MM-DD') as dbday,
            sal,deptno
            FROM emp 
            WHERE deptno=30
            ORDER BY sal DESC
        """
    cur.execute(sql)
    list=cur.fetchall()
    print(list)
    emp =pd.DataFrame(list)
    print(emp)
    colname=cur.description
    print(colname)

    cur.close()
    conn.close()

    col=[]
    for i in colname:
        col.append(i[0].lower())
    emp=pd.DataFrame(list,columns=col)
    print(emp)
    emp.plot.scatter(x='ename',y='sal',s=100,c='purple')
    #plt.show()
    plt.savefig('c:/vuejs/emp.png')
empGraphData()