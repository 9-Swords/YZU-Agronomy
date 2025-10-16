num=100
i=0
while num<1000:
    x=num//100
    y=num//10%10
    z=num%10
    if num==x**3+y**3+z**3:
        i=i+1
        print("第",i,"个水仙花数是：",num)
    num=num+1
print("水仙花数共有",i,"个")
