'''





dan=int(input("2~9단 사이의 정수 입럭:"))
def gugudan(dan):
    for i in range(1,10):
        print(f"{dan}*{i}={dan*i}")

gugudan(dan)
'''
'''
def emp_list():
    emp=["홍길동","심은하","타노스","짱구","김똘똘"]
    return emp,emp.__len__()

emp,total=emp_list()
for name in emp:
    print(name)
print(f"인원{total}")

def defaultFunc(a=10,b=20,c=30):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")

defaultFunc(100)
defaultFunc(100,200)
defaultFunc(100,200,300)

def changeFunc(*args):
    for i in args:
        print(f"i={i}")
changeFunc(1)
changeFunc(1,2)
changeFunc(1,2,3)
changeFunc(1,2,3,4,5,6,7)
'''