"""
 pip install numpy
 pip install pandas
 pip install matplotlib = seaborn
 Numpy
 ------
   1. 복잡한 배열 / 행렬 계산
   2. 난수 생성이 가능 '
   3. 연산을 위한 라이브러리
   import numpy as np
"""
# 리스트에서 행렬 / 배열 생성
import numpy as np

# [] = 배열 = numpy 변경
a = [[1, 2, 3], [4, 5, 6]]  # 리스트에서 행렬 생성 => 2차원 배열
b = np.array(a)  # 넘파이 배열로 변경 => array()
print(a)
print(b)
# 배열의 열수(차원)
print(b.ndim)
# 배열의 차원 = 행 / 열 => 2행 3열 => (2,3)
print(b.shape)
# 배열의 원소 접근
print(b[0, 0])
"""
          0     1    2
     ----------------------
   0      1     2    3
         0,0   0,1  0,2
     ----------------------
   1      4     5    6
         1,0   1,1  1,2
     ----------------------
"""
"""
for i in range(0,2):
    for j in range(0,3):
        print(b[i,j],end=" ")
    print()
"""
# 특수한 배열의 생성
print(np.arange(10))  # 1씩 증가하는 1차원 배열 (시작은 0부터)
print(np.arange(5, 10))  # 1씩 증가하는 1차원 배열 (시작은 5부터)
print(np.zeros((2, 2)))  # 0으로 채운다 => 행렬 => float
print(np.ones((2, 3)))  # 2행 3열 배열 생성
print(np.full((2, 3), 5))
# 나중에 값을 채워서 사용 np.array([[0,0,0],[0,0,0]])
# 배열의 차원 변환
a = np.arange(20)  # 1차원
print(a)
b = a.reshape((4, 5))  # 4행 5열 배열 생성
print(b)
# Numpy 슬라이싱(자르기) / 인덱싱
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)
a = arr[0:2, 0:2]
print(a)
# numpy => 연산처리를 위한 라이브러리
# 1. 배열간 연산 기능 => + / - / / *
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # list는 배열을 통합
c = np.array(a)
d = np.array(b)
e = c + d
print(e)
e = np.add(c, d)
print(e)
# + => add
e = c * d
print(e)  # [4,10,18]
e = np.multiply(c, d)
print(e)
# * => multiply
e = c / d  # 1/4 = 0.25 , 2/5 0.4 , 3/6 0.5
print(e)
e = np.divide(c, d)
print(e)
# / => divide
# 행렬 => dot() = 행렬의 곱
"""
   [[1,2],[3,4]]
   [[5,6],[7,8]]

   1*5 + 2*7  , 1*6+2*8
     5+14        6+16  
   3*5 + 4*7  , 3*6+4*8
     15+28       18+32

   수학 계산 = 행렬 
"""
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
c = np.array(a)
d = np.array(b)
e = np.dot(c, d)
print(e)

# 모든 배열 값의 합  sum(), 곱 prod()
a = np.array([[-1, 2, 3], [3, 4, 8]])
s = np.sum(a)
print(s)
p = np.prod(a)
print(p)
# 평균 mean() / 표준 편차 std
# => 19/6
m = np.mean(a)
print(m)
ss = np.std(a)
print(ss)
"""
  10  8  10  8  8  4
  sum : 48
  mean : 48/6 => 8 
  분산
    10   8  10  8  8  4
    -8  -8 -8  -8 -8 -8
    --------------------
     2   0  2   0  0  4
     ------------------
     2^2   2^2       4^2
       4    4         16 ===> 24
     24 / n-1 => 24/5 => 4.8 


  표준편차 
    4.8 루트 => 2... => std
"""