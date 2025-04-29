import pymysql as pm
import oracledb as db
'''
#1. connection 객체 생성
conn=pm.connect(host="localhost",user="root",password="happy",db="mydb",charset="utf8")
#2. preparedstatement 생성
cur=conn.cursor()
#3. SQL 문장 전송 => 실행
sql=f"""
    SELECT empno,ename,job,
    date_format(hiredate,'%Y-%m-%d') as regdate,
    sal,dname,loc
    FROM emp JOIN dept
    ON emp.deptno=dept.deptno
    
    """
cur.execute(sql)
#4. 결과값 얻기
emp_join=cur.fetchall()
#5. 함수 = return

#6. cursor/connection 닫기
cur.close()
conn.close()
#7. 데이터 출력
print(emp_join)
for row in emp_join:
    data=list(row)
    print(data)
#8. 데이터프레임 변경

#9. 시각화
#10. 이미지화 => 스프링의 realpath
#subquery
#like
'''
# subquery
'''     1 SQL
        *DQL : SELECT
        *DML : INSERT UPDATE DELETE
        DCL : GRANT REVOKE
        DDL : CREATE DROP ALTER RENAME TRUNCATE
        *TCL : COMMIT / ROLLBACK
'''
'''
findData=input("이름 입력:")
conn=pm.connect(host="localhost",user="root",password="happy",db="mydb",charset="utf8")
cur=conn.cursor()
sql=f"""SELECT empno,ename,job,date_format(hiredate,'%Y-%m-%d') as hiredate,
        sal,dname,loc
        FROM emp,dept
        WHERE emp.deptno=dept.deptno
        AND ename LIKE concat('%','{findData}','%')
    """
cur.execute(sql)
data=cur.fetchall()
cur.close()
conn.close()
for s in data:
    data1=list(s)
    print(data1)

'''
'''
conn=pm.connect(host="localhost",user="root",password="happy",db="mydb",charset="utf8")
cur=conn.cursor()

sql =f"""
     SELECT empno,ename,job,hiredate,sal,
    (SELECT dname FROm dept WHERE deptno=emp.deptno) as dname,
    (SELECT loc FROm dept WHERE deptno=emp.deptno) as loc
    FROM emp
    """
cur.execute(sql)
data=cur.fetchall()
cur.close()
conn.close()
for s in data:
    d=list(s)
    print(d)
    '''
'''
conn=pm.connect(host="localhost",user="root",password="happy",db="mydb",charset="utf8")
#conn=db.connect("hr/happy@localhost:1521/xe")
cur=conn.cursor()

param=(7788,)
sql="SELECT * FROM emp WHERE empno=%s"
 cur.execute(sql,param)
data=cur.fetchall()
cur.close()
conn.close()
print(data)
'''

#수정
conn=pm.connect(host="localhost",user="root",password="happy",db="mydb",charset="utf8")
cur=conn.cursor()
sql=f"""
     UPDATE student SET
     name=%s , kor=%s , eng=%s , math=%s
     where hakbun=%s
    """
param=('홍길동 수정',90,90,90,1)
cur.execute(sql,param)
conn.commit()
print("수정 완료")
