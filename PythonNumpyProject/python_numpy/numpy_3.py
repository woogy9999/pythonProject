

"""
    1차
    1. MVC
    2. Ajax (jquery)
    3. mybatis
    4. session / cookie

    2차
    1. Spring Framework
    2. MVC
    3. Mybatis = CRUD
    4. Vue
    5. 보안

    1. 협업 => mainpage => GIT => 공통작업페이지

    => 과정 : 파이썬 , Elasticsearch
    => AWS호스팅
    => React / React-Query / Redux
    => Doker / AWS기반
    => JPA / MySQL / Spring-Boot
    => CICD

"""
import numpy as np
a=np.array([1,2,3,4,5])

b=a[0]
c=a[1]
for i in range(len(a)):
    print(a[i])

d=a[1:4] # 2 3 4
print(d)
e=a[:3] # 인덱스 0,1,2 => 123
f=a[3:] # 4,5
print(e,f)

arr=np.array([[1,2,3],[4,5,6]])
a=arr[0,0] # 1
b=arr[1,2] # 6
print(a,b)

a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.concatenate((a,b))
print(c)

a=np.array([1,2,3,4,5,6])
b,c=np.split(a,[3])
print(b,c)
