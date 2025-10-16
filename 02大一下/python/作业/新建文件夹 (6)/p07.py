ls=input("请输入列表中的一串数据：")
f=lambda x:x*x
s=0
for i in ls:
    if i>="0" and i<="9":
        s+=f(int(i))
print("该组数据的平方和为：",s,sep="")

