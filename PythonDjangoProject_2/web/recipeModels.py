from turtledemo.penrose import start

from django.db import models
import oracledb as db
from web import models


def recipeListData(page):
    try:
        conn = models.getConnection()
        cur = conn.cursor()
        rowSize=12
        start=(rowSize*page)-(rowSize-1)
        end=(rowSize*page)
        sql = f"""
            SELECT no,title,poster,chef,num 
            FROM (SELECT no,title,poster,chef,rownum as num
            FROM (SELECT /*+ INDEX_ASC(recipe recipe_no_pk)*/no,title,poster,chef
            FROM recipe WHERE no IN(SELECT no FROM recipe
            INTERSECT SELECT no FROM recipeDetail)))
            WHERE num BETWEEN {start} AND {end}
            """

        cur.execute(sql)
        recipe_list=cur.fetchall()

        cur.close()
        cur=conn.cursor()
        sql=f"""
            SELECT CEIL(COUNT(*)/12.0)
            FROM recipe
            WHERE no IN(SELECT no FROM recipe
                INTERSECT SELECT no FROM recipeDetail)
            """
        cur.execute(sql)
        total=cur.fetchone()
    except Exception as e:
        print(e)
    finally:
        models.disConnection(conn,cur)

    return recipe_list,total[0]

def recipeDetailData(no):
    try:
        conn=models.getConnection()
        cur=conn.cursor()
        sql=f"""
               SELECT no,title,chef,chef_poster,chef_profile,
               info1,info2,info3,content,poster,foodmake,data
               FROM recipedetail
               WHERE no={no}
            """
        cur.execute(sql)
        recipe_detail=cur.fetchone()
        #CLOB (Object => str)
        rmake=''.join(recipe_detail[-2].read())
        rdata=''.join(recipe_detail[-1].read())
    except Exception as e:
        print(e)
    finally:
        models.disConnection(conn,cur)

    return recipe_detail,rmake,rdata

