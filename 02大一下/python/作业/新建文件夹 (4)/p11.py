ls=input("请输入英文字符串：")
a=ls.lower()
b=[x for x in a if x>="a" and x<="z"]
c=[x for x in b if b.count(x)==1]
for x in b:
    if b.count(x)>1 and c.count(x)==0:
        c.append(x)
c.sort()
cgai=",".join(str(i) for i in c)
print(cgai)
