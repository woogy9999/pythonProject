import oracledb as db
import matplotlib.pyplot as plt
import pandas as pd

conn=db.connect('hr/happy@localhost:1521/xe')
cur=conn.cursor()
sql=f"""
        SELECT name,hit FROM project_food
        ORDER BY hit DESC
     """

cur.execute(sql)
food=cur.fetchall()
cur.close()
conn.close()
#print(food)
column=['업체명','조회수']
list=pd.DataFrame(food,columns=column)
#print(list)
top10=list.sort_values(by='조회수',ascending=False).head(10)
#print(top10)
plt.figure(figsize=(10,10))
plt.rc('font',family='Malgun Gothic')
plt.bar(top10['업체명'],top10['조회수'])
plt.title("맛집별 조회수 TOP10")
plt.xticks(rotation=90)
plt.show()
