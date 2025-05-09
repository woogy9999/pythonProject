from django.db import models

# Create your models here.
import oracledb as db

def getConnection():
    try:
        conn=db.connect("hr/happy@localhost:1521/XE")
    except Exception as e:
        print(e)
    return conn

def disConnection(conn,cur):
    try:
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
def foodListData(page):
    try:
        rowSize=12
        start=(rowSize*page)-(rowSize-1)
        end=(rowSize*page)

        #연결
        conn=getConnection()
        cur=conn.cursor()

        sql=f"""
                SELECT fno,name,poster,num
                FROM (SELECT fno,name,poster,rownum as num
                FROM (SELECT fno,name,poster
                FROM project_food ORDER BY fno ASC))
                WHERE num BETWEEN {start} AND {end}
            """
        cur.execute(sql)
        food_list=cur.fetchall()
        cur.close()
        cur = conn.cursor()

        sql=f"""
                SELECT CEIL(COUNT(*)/12.0) FROm project_food
            """
        cur.execute(sql)
        total=cur.fetchone()
    except Exception as e:
        print(e)
    finally:
        disConnection(conn,cur)

    return food_list,total[0]

# 상세보기
def foodDetailData(fno):
    try:
        conn=getConnection()
        cur=conn.cursor()
        sql=f"""
              SELECT fno,name,poster,score,address,phone,
              parking,time,type,theme,content
              FROM project_food 
              WHERE fno={fno}
            """
        cur.execute(sql)
        food_detail=cur.fetchone()
        content=''.join(food_detail[-1].read())
        theme = ''.join(food_detail[-2].read())
    except Exception as e:
        print(e)

    finally:
        disConnection(conn,cur)
    return food_detail,content,theme