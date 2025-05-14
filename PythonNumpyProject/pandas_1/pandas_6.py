"""

    Numpy
    = pip install numpy
    = import numpy as np
    1. list => np.array()
    2. 특수 배열
       np.zeros / np.ones / np.arange
       np.linespace(0,10,5)
    3. 난수
    randint() : 정수 추출
    rand() : 0~1 사이의 실수
    4. 배열 연산
       +  , - , * , /
       a=np.array([10,20,30])
       b=np.array([1,2,3])

"""
import numpy as np
import pandas as pd

"""
import numpy as np
a=np.array([1,2,3,4,5])
print(a)
line=np.linspace(0,10,5)
print(line)
"""
# 특정 조건에 맞는 인덱스
arr=np.array([1,2,3,4,5])
index=np.where(arr>3)
print(arr[index])
""" 
    Pandas : 데이터 분석 / 데이터 조작을 위한 라이브러리 
    = 엑셀 , CSV , SQL , JSON
      데이터를 쉽게 처리가 가능하게 만든 라이브러리
    = 데이터 구조
      1. DataFrame : 테이블 형태 (2차원 배열)
                     = column / row
"""
data=[1,2,3,4,5]
series=pd.Series(data)
print(series)

# 원하는 인덱스로 지정이 가능
# 기본적으로 숫자 인덱스(0)가 할당된다
data=[100,200,300]
index_lab=["a","b","c"]
series=pd.Series(data,index=index_lab)
print(series)
print(series['a'])