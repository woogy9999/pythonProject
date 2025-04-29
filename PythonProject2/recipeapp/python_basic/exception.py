'''
    예외처리 : 에러를 방지하고 정상 졸료를 수행 ( 비정상 종료 방지 )

    1. 파이썬에서 제공하는 예외처리
                BaseException (Throwable)
                        |
                -----------------------------
                |                           |
            (Error)                     (Exception)
            => 수정이 불가능              => 에러 수정이 가능
            SystemExit                          |
            KeyboardInterrupt                   |
                                        ArithmeticError
                                            => FloatingPointError
                                            => Overflow
                                            => ZeroDivisionException
'''
from warnings import catch_warnings

'''
def display():
    print(1)
    print(2)
    try:
        print(3)
        print(4)
        print(10/0)
        print(5)
    except Exception as e:
        print("6에러 발생:",e)
    finally:
        print(7)
    print(8)

display()
    
'''
''' 
    def list(page){
        try:
            page=request.Get['page']
        :except Exception as e:
            page="1"
'''

def div(a,b):
    return a/b

try:
    c=div(5,2)
    print(c)
   # c=div(5,0)
    print(c)

    e=[2,3]
    print(e[0])
    print(e[1])
   # print(e[3])

    f=open('c:/pydate/upload.txt')

except Exception as e:
    print("에러메세지",e)
except ZeroDivisionError as e:
    print("에러메세지",e)
except IndexError as e:
    print("에러메세지",e)
finally:
    print("무조건 수행")
