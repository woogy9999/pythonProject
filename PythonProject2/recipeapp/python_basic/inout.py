'''
    파일 입출력
    => 특화된 언어 (데이터 수집) = 파일 저장
    => 데이터 분석 (Numpy, Pandas, konlp) => 형태소 분석
    => 웹사이트는 많이 사용하지 않는다
        | 스프링과 연동 , MSA
        ------------------- 웹 = 웹 연결 (JSON)
    형식) 파일 => 단방향 / 읽기 / 쓰기
            1. 파일열기
                f=open(경로명,모드) => c:\ c:/
                             ----
                             w(생성/쓰기) / r(읽기) / a(추가)
            2. 파일 닫기
                f.close()
'''
def writedata():
    try:
        f=open("c:/pydata/student.txt",'a') #=> w:create파일 생성 내용저장
        for i in range(1,11):
            data="홍길동 %d\n" %i
            f.write(data)
        f.close()
        print("파일 저장 완료")
    except Exception as e:
        print("파일 에러:",e)

writedata()