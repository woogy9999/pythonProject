'''
    제어문
    elif 조건문

    2) 반복문
      = for
      = while

    3) 반복제어문
      = break

'''

import random

# 단일 조건문
rand = random.randrange(1, 101)

if (rand % 2 == 0):
    print(f"{rand}는 짝수입니다")
if (rand % 2 != 0):
    print(f"{rand}는 홀수입니다")

if (rand % 2 != 0):
    print(f"{rand}는 홀수입니다")
else:
    print(f"{rand}는 짝수입니다")

if rand > 90:
    print("A")
elif rand >= 80:
    print("B")
elif rand >= 70:
    print("C")
elif rand >= 60:
    print("D")
else:
    print("F")
