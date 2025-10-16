d={1:("李雷","张玉","王晓刚","陈红静","方向","司马清"),
   2:("施然","李芳芳","刘潇","方向","孙一航","黄煌"),
   3:("陈红静","方向","刘培良","张玉","施小冉","司马清")}
c=[]
for v in d.values():
    for x in v:
        c.append(x)
d1={}
for x in c:
    d1[x]=d1.get(x,0)+1
print("这个班有{}位学生没有选课".format(25-len(d1)))
d2=0
d3=0
d4=0
for v in d1.values():
    if v==2:
        d2+=1
    elif v==3:
        d3+=1
    else:
        d4+=1
print("有{}位学生同时选修了2门课".format(d2))
print("有{}位学生同时选修了3门课".format(d3))
print("有{}位学生同时选修了1门课".format(d4))
