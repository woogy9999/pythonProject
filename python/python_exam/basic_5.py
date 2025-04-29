'''money=1000
age=25
if money>=500:
    item="사과"
    if age<=30:
        msg="new"
    else:
        msg="old"
print(item,msg)
'''
'''
i=1
while i<=10:
    print("i=%d" %i)
    i+=1

i=1
while i<=10:
    if i%2==0:
        print("i=%d" %i)
    i+=1

sum=0
i=1
while i<=100:
    if i%2==1:
        print(f"i={i}")
    i+=1
'''
'''
sum=0
even=0
odd=0
i=1
while i<=100:
    if i%2==0:
        sum+=i
        even+=i
    else:
        sum+=i
        odd+=i
        print(i)
    i+=1
print(f"sum={sum}")
print(f"even={even}")
print(f"odd={odd}")
'''
'''
for i in range(1,10,2):
    print(f"i={i}")

list=["red","blue","yellow","black","green"]
for color in list:
    print(color)
print("=============")
for _ in (range(5)): #5바퀴
    print("hello")
    
'''
