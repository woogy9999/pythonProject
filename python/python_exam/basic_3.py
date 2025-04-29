'''
  변수 설정 :
    변수 = 값 (데이터형을 사용하지 않는다)
            반드시 초기값을 부여

'''
'''
# 치환 연산자 (대입연산자)
a = 10
# 복수의 주소에 저장
b = c = d = 10  # int a,b,c; a=b=c=10
e, f = 100, 200

# 산술연산자
a = 10
b = 3
print(a)
print(b)
print(e, f)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

name1 = '홍'
name2 = '길동'
print(type(name1))
print(type(name2))
print('홍' + '길' + "동")
print('홍' * 10)
print(10.5 + float(10))
print(10 + 10.5)
print(bool(''))
print(bool(0))
# 문자열은 공백을 제외한 모든 문자는 True
'''
a = 10
b = 9
print(a==b)
print(a is b)
print(a!=b)

# 조건문 / 반복문 => True/False
