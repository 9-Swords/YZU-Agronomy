def myfunc(x,n):
    s=0
    for i in range(1,n+1):
        s=s+int(x*i)
    return s
x=input("请输入x的值：")
n=eval(input("请输入n的值："))
print(myfunc(x,n))
        
