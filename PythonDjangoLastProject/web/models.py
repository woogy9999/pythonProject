from django.db import models
import oracledb as db
import json


# Create your models here.

def getConnection():
    try:
        conn = db.connect("hr/happy@localhost:1521/XE")
    except Exception as e:
        print(e)
    return conn


def disConnection(conn, cur):
    try:
        cur.close()
        conn.close()
    except Exception as e:
        print(e)

def mainPageData():
    try:
        conn=getConnection()
        cur=conn.cursor()
        sql=f"""
            SELECT fno,name,poster,rownum 
            FROM (SELECT fno,name,poster
            FROM project_food ORDER BY fno ASC)
            WHERE rownum<=12    
            """
        cur.execute(sql)
        food_list=cur.fetchall()
        cur.close()

        cur = conn.cursor()
        sql = f"""
                    SELECT no,title,poster,rownum 
                    FROM (SELECT no,title,poster
                    FROM recipe ORDER BY no ASC)
                    WHERE rownum<=12    
                    """
        cur.execute(sql)
        recipe_list = cur.fetchall()
    except Exception as e:
        print(e)
    finally:
        disConnection(conn,cur)
    return food_list,recipe_list
