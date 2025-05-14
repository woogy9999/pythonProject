import pandas as pd
import numpy as np
import csv

"""
   GPT = 2년/3년차 = 셋팅 
   아나콘다 / juter note book / vscode 
   ------------------------- 머신러닝 / 딥러닝 
   파이참 : 커뮤니티 
   => 문자열 : 모든 데이터 
   => 컴파일 없이 인터프리터 : 한줄씩 번역후 출력 

   53페이지 
    기본 문법 
    --------
    변수 = 데이터형을 사용하지 않는다 
          => type을 이용하면 어떤 데이터형인지 확인 
          => <class 'int'> 
                     'float'
                     str
                     bool
          => 데이터형 인식 : class형으로 인식 
    연산자 : + : 문자열 결합 
                문자+문자 
                    ---- 숫자 str(10)
            / : 결과값 실수 
            // : 결과값 정수 
            ** : 거듭 제곱 

            !는 사용하지 않는다 => not 
            && => and
            || => or 

            형변환 : 정수 => int()
                    실수 => float()
                    문자 => str()
                    논리 => bool()
                           --------
                           1. 0,0.0을 제외한 모든 수는 True
                           2. null값을 제외한 문장 True
    제어문 
      if 
      if 조건문:
         처리문장 => 들여쓰기 

      if ~ else
      if 조건문:
         처리문장 
      else:
         처리문장 

      초기값 
      while 조건문:
         반복 수행문장
         증가식 => i++(X) => i+=1  i=i+1

         ++,-- ! , ()
         ----- not int() , float() ...
         i+= i-=

      for 받는 변수 in list,tuple,str:
           처리문장 
      for 받는 변수 in range(1,10) 1~9

      => round() => 반올림 함수 
         round(실수,소수점 자리수)  => 56

    ------------------------------------
    함수 / 예외처리 
    함수 : 명령문의 집합 => 한개의 기능을 수행하는 영역 
          => 다른 파일과 연결 , 클래스간의 연결 
          => 목적 : 재사용 
          => 기능 : 구조화된 프로그램 
          함수 : 독립적으로 사용이 가능 : C/파이썬/JavaScript
          메소드 : 클래스 종속 
    def 함수명(매개변수...):
          기능 처리 
          리턴이 있는 경우 => 여러개를 동시에 전송이 가능
          return 값
     예)
         def data():
           return "aaa",10,False

         s,i,b=data()
     예외처리 : 사전에 에러 방지 
               비정상 종료를 방지하고 정상 상태 유지 
     try:
         정상 수행 문장 
     except Exception as e:
         예외에 복구 => 확인 
     finally: 
         서버 닫기 / 파일 닫기 / 데이터베이스 닫기 75page 

    변수 / 연산자 / 제어문 / 함수 / 예외처리 
    ----------------------------------- 기본 문법 
    => 라이브러리 
       pip 라이브러리 설정 
    99page 파일 입출력 
           a , w , r
           ----- 파일이 없는 경우에 자동으로 생성 
           a = append 
           w = write => set
           r = read

           open => close

           => 1. txt 
              2. csv 
              3. 액셀 
              4. xml 
              5. json 
    => 정규식 
    => 크롤링 
    => 판다식 사용 
    => 시각화 

"""
# print(round((90+90+80+88+77)/6,2))
# 104 page
file = open('c:/pydata/EMP.csv')
emp = csv.reader(file)
# print(emp)
"""
=> INITCAP 
for i in emp:
    print(i[1].title())
"""
# 문자열 길이 확인
"""
for i in emp:
    print(i[1],len(i[1]))
"""
# 문자열 결합
"""
   empno ename job mgr hiredate sal comm deptno
     0     1    2   3     4      5    6     7
"""
for i in emp:
    print(f"{i[1]}의 급여는 {i[5]}")
file.close()