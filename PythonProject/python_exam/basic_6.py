for i in range(1,10):
    for j in range(2,10):
        print(f"{j}*{i} = {i*j}",end="\t")
    print()



for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()

print()
i=0
j=0
for i in range(1,10,2):
    for j in range(10 -i):
        print("*",end="")
    print()

