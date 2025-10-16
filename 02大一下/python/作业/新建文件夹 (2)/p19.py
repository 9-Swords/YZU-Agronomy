import random
c=0
for x in range(5):
    for i in range(100000):
        a=random.randint(1,6)
        b=random.randint(1,6)
        if a+b==7:
            c=c+1
    print(c/100000,end=" ")
