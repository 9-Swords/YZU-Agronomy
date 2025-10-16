def f(n):
    s=0
    for i in n:
        s=s+int(i)
    return s
n=input("请输入一个正整数：")
print("各位数字和为：",f(n),sep="")
