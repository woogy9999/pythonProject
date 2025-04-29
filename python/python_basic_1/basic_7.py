import pymysql as pm



def getConnection():
    conn=pm.connect(host="localhost",user="root",password="happy",db="mydb",charset="utf8")

    return conn

def disConnection(conn,cur):
    cur.close
    conn.close

def empListData():
    conn = getConnection()
    cur = conn.cursor()
    sql="""SELECT empno,ename,sal,job,
            date_format(hiredate,'%Y-%m-%d') as hiredate,
            dname,loc
            FROM emp JOIN dept
            ON emp.deptno=dept.deptno
        
        """
    cur.execute(sql)
    emp_list=cur.fetchall()
    print(emp_list)
    disConnection(conn,cur)
    return emp_list

def empFindData(ename):
    conn=getConnection()
    cur=conn.cursor()
    sql=f"""
        SELECT * FROM emp
        WHERE ename LIKE concat('%','{ename}','%')
        """
    cur.execute(sql)
    emp_list=cur.fetchall()
    disConnection(conn,cur)
    return emp_list

def empDetailData(empno):
    conn = getConnection()
    cur = conn.cursor()
    sql = f"""
            SELECT empno,ename,job,
            date_format(hiredate,'%Y-%m-%d'),sal
            FROM emp
            WHERE empno={empno}
            """
    cur.execute(sql)
    emp_data=cur.fetchone()
    disConnection(conn,cur)
    return emp_data

#추가
def deptInsert(dept):
    conn=getConnection()
    cur=conn.cursor()
    sql="""
        INSERT INTO dept
        VALUES(%s,%s,%s)
        """
    cur.execute(sql,dept)
    conn.commit()
    print("데이터 추가 완료")
    disConnection(conn,cur)

def deptUpdate(dept):
    conn=getConnection()
    cur=conn.cursor()
    sql="""
        UPDATE dept SET
        dname=%s, loc=%s
        WHERE deptno=%s
        
        """
    cur.execute(sql,dept)
    conn.commit()
    print("데이터 수정 완료")
    disConnection(conn,cur)

def deptDelete(deptno):
    conn=getConnection()
    cur=conn.cursor()
    sql="""
        DELETE FROM dept
        WHERE deptno=%s
        """
    cur.execute(sql, deptno)
    conn.commit()
    print("데이터 삭제 완료")
    disConnection(conn, cur)

def main():
    while(True):
        print("1.사원 목록")
        print("2.사원 검색")
        print("3.상세 보기")
        print("4.데이터 추가")
        print("5.데이터 삭제")
        print("6.데이터 수정")
        print("7.종료")
        menu=int(input("메뉴 선택:"))
        if menu==7:
            print("프로그램 종료")
            break
        elif menu==1:
            emp_list=empListData()
            for emp in emp_list:
                e=list(emp)
                print(e)
        elif menu==2:
            ff=input("검색어 입력 :")
            emp_list=empFindData(ff)
            for emp in emp_list:
                e=list(emp)
                print(e)
        elif menu==3:
            empno=input("사번 입력 :")
            emp_data=empDetailData(empno)
            for emp in emp_data:
                e=list(emp)
                print(e)
            print(f"사번:{emp_data[0]}")
            print(f"이름:{emp_data[1]}")
            print(f"직위:{emp_data[2]}")
            print(f"입사일:{emp_data[3]}")
            print(f"급여:{emp_data[4]}")
        elif menu==4:
            dept=(50,'영업부','부산')
            deptInsert(dept)
        elif menu==6:
            dept=('기획부','서울',50)
            deptUpdate(dept)
        elif menu==5:
            deptno=('50')
            deptDelete(deptno)
main()