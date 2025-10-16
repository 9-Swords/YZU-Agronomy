i=1
n=0
pi=0
while 1/i>1e-6:
    pi=pi+4*(1/(i*((-1)**n)))
    i=i+2
    n=n+1
print("pi的近似值为：",pi)
