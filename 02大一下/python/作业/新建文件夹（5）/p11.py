s="Whether the weather be fine,or whether the weather be not. Whether the weather be cold, or whether the weather be hot. We will weather the weather whether we like it or not."
x=s.lower()
a=x.replace(","," ")
b=a.replace("."," ")
c=b.split(" ")
d={}
for x in c:
    if x!="":
        d[x]=d.get(x,0)+1
print("该字符串中英文单词个数为：{}".format(len(d)))


