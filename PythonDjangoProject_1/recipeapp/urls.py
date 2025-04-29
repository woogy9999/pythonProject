'''
    django-admin startproject : 장고 프로젝트 생성 명령
    startapp : 프로젝트의 기능 설정
    migrate : 데이터베이스 설정
    runserver : 서버 구동
    models.py : 데이터베이스 연동 (DAO)
    view.py : 데이터를 HTML전송
    urls.py : 화면 이동
    templates = html이 저장되는 폴더명

    manage.py => 파이썬 명령어 사용시 사용되는 파일
    settings => 데이터베이스 설정 , Cross Origin , static 설정
'''
from tkinter.font import names

from django.urls import path
from recipeapp import views

#@requestMapping
urlpatterns=[
    path('',views.index,name="index"),
    path('recipe_list/',views.recipeList,name="recipe_list"),
    path('recipe_detail/',views.recipeDetail,name="recipe_detail")
]

