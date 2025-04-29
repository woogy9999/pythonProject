'''

    함수 : 한개의 기능을 모아서 재사용이 가능
        = 명령문을 모아서 처리
        = 변수 , 연산자 , 제어문
        = 기능 한개만 수행이 가능
        = 종류
            1) 라이브러리 : 제공 => 필요시마다 재사용
                print , range ... append
            2) 사용자 정의
            = 리턴형
            = 매개변수
            = 함수명 : 변수의 식별자와 동일
            = 형식
              def 함수명(매개변수..):
                  처리
                  return...
            => function 함수명 (매개변수..)
            => fun 함수명(매개변수){} => 코틀린
               var(변수),val(상수)

            매개변수 => 가변 매개변수
                       def 함수명(*args) => ...
                         함수명(1) 함수명(2) 함수명(1,2,3)
                        default 매개변수
'''

def sort():
    data=[30,20,50,40,10]

    print(f"정렬전:{data}")
    for i in range(len(data)-1):
        for j in range(i,len(data)):
            if data[i]>data[j]:
                temp=data[i]
                data[i]=data[j]
                data[j]=temp

    print(f"정렬후:{data}")
sort()

def getInfoData():
    return "홍길동"

name=getInfoData()
print(name)

def getInfoData2():
    return "심청이",25,"여자"
name,age,sex=getInfoData2()
print(f"이름:{name}")
print(f"나이:{age}")
print(f"성별:{sex}")