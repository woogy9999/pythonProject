import oracledb

conn=oracledb.connect('hr/happy@localhost:1521/XE')

cursor=conn.cursor()
sql=f"SELECT * FROM emp"
cursor.execute(sql)

for row in cursor:
    print(row)
cursor.close()
conn.close()