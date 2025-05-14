import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt

mpl.rc('font',family='Malgun Gothic')
mpl.rc('axes',unicode_minus=False)

# 타이타닉 => 그래프를 한번에 여러개
sns.set(font='Malgun Gothic',rc={'axes.unicode_minus':False} , style='darkgrid')
plt.rc('figure',figsize=(10,8))
"""
np.random.seed(10)
df1=pd.DataFrame(np.random.randn(100,3),
      index=pd.date_range('1/1/2025',periods=100),columns=['A','B','C']).cumsum()
print(df1)
df1.plot()
plt.title('pandas random 사용')
plt.xlabel("시간")
plt.ylabel("데이터")
plt.show()
"""
# 연습용 데이터셋
iris=sns.load_dataset('iris')
titanic=sns.load_dataset('titanic')

#     sepal_length  sepal_width  petal_length  petal_width    species
#print(iris)
#     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
#print(titanic)
"""
s1=iris.sepal_length[:20]
s1.plot(kind="bar",rot=0)
plt.title("받침대의 길이")
plt.xlabel("데이터")
plt.ylabel("꽃받침 길이")
plt.show()
"""
"""
    xlim : x축의 범위
    ylim : y축의 범위
    axis : x,y 동시 지정
    
    axis => equal : x,y축의 비율을 실제와 동일하게
            on : 생략시
            off : 축,이름 제거
            scaled : x,y축의 비율을 실제와 동일하게 , 여백 축소
"""
"""
df2=iris[:5]
df2.plot.bar(rot=0)
plt.title('Bar Plot')
plt.xlabel("데이터")
plt.ylabel("각 Featrue 값")
plt.ylim(0,7)
plt.show()
"""
"""
    SELECT COUNT(*) SUM(),AVG(),MAX(),MIN()
    FROM emp
    GROUP BY deptno
    
"""
"""
df3=iris.groupby(iris.species).mean()
print(df3)
df3.plot.bar(rot=0)
plt.title("각 꽃 종류별 평균")
plt.xlabel("평균")
plt.ylabel("종류")
plt.ylim(0,8)
plt.show()
"""
"""
df4=titanic.pclass.value_counts()
print(df4)
df4.plot.pie(autopct="%.2f%%")
plt.title("선실별 승객 수 비율")
plt.axis('equal')
plt.show()
"""
"""
iris.plot.hist()
plt.title("Histogram")
plt.xlabel("데이터값")
plt.show()
"""
"""
iris.plot.box()
plt.title("Box Plot")
plt.xlabel("종류")
plt.ylabel("데이터값")
plt.show()
"""
iris.boxplot(by="species")
plt.tight_layout(pad=3,h_pad=1)
plt.suptitle("Box Plot")
plt.show()