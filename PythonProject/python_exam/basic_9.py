'''
    집합 데이터형 (자바 => Collection)
    1. list => List / ArrayList , Array
        = 중복데이터를 허용
        = 인덱스 번호 => 순서가 존재
        = name=["","","",""] => 그래프 작업
          일차원 배열

          데이터 수집 ( 크롤링,데이터베이스 )
                     |
                데이터를 모아서 관리 (CSV,TXT)
                    |
                분석 (Numpy, Pandas)
                    |
                시각화 (Matplotlib,Seaborn)
                    |
                완료 => 데이터베이스 누적
'''

names = ["홍길동", "심은하", "강해상", "도라에몽","마동석"]
print(names)
'''
for name in names:
    print(name)

print(f"인원:{len(names)}")
# 추가 append => 마지막에 추가
names.append("을지문덕")
names.append(1,"김두한")
print(names)
'''
# 여러개를 동시에 추가
#names.extend(["김우신","홍홍홍"])
#print(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names)
# 삭제
names.remove("홍길동")
print(names)

# 정렬
# 역순 출력
