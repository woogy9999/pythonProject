import sqlite3

class StudentVO:
    def __init__(self, hakbun=0, name='', kor=0, eng=0, math=0):
        self.hakbun = hakbun
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

class StudentDAO:
    conn=None
    cursor=None

    def __init__(self):
        print("생성자 함수 호출")

    def __del__(self):
        print("소멸자 함수 호출")

    def getConnection(self):
        self.conn=sqlite3.connect("student.db")
        self.cursor=self.conn.cursor()
    def disConnection(self):
        self.conn.close()

    def dbCreate(self):
        self.getConnection()
        sql="""
            CREATE TABLE IF NOT EXISTS student(
            hakbun int,name text,kor int,eng int,math int)
            """
        self.cursor.execute(sql)
        self.disConnection()

    def insert(self,vo):
        self.getConnection()
        data=(vo.hakbun,vo.name,vo.kor,vo.eng,vo.math)
        sql="INSERT INTO student VALUES(?,?,?,?,?)"
        self.cursor.execute(sql,data)
        self.conn.commit()
        print("학생 등록 완료")
        self.disConnection()

    def selectList(self):
        self.getConnection()
        sql="SELECT * FROM student"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        self.disConnection()
        return data

    def delete(self, hakbun):
        self.getConnection()
        sql = f"DELETE FROM student WHERE hakbun = {hakbun}"
        self.cursor.execute(sql)
        self.conn.commit()
        self.disConnection()
    def selectOne(self,hakbun):
        self.getConnection()
        sql=f"SELECT * FROM student WHERE hakbun={hakbun}"
        self.cursor.execute(sql)
        data=self.cursor.fetchone()
        self.disConnection()
        return data

dao=StudentDAO()
"""
print("dao객체 생성")
dao.dbCreate()
print("데이터베이스 테이블 생성!!!")
"""
"""
vo=StudentVO()
vo.hakbun=int(input("학번입력:"))
vo.name=(input("이름입력:"))
vo.kor=int(input("국어입력:"))
vo.math=int(input("수학입력:"))
vo.eng=int(input("영어입력:"))
dao.insert(vo)
print("학생 입력 완료")
"""

hakbun=int(input("상세볼 학번:"))
data=dao.selectOne(hakbun)
print(data)
"""
hakbun=int(input("삭제할 학번:"))
dao.delete(hakbun)
print("삭제완료")

data=dao.selectList()
for row in data:
    print(row)
"""