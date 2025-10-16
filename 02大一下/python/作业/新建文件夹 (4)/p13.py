lst_weather=[['周一', '16℃', '26℃', '多云', '1级', '优'],
             ['周二', '17℃', '27℃', '晴', '2级', '优'],
             ['周三', '16℃', '28℃', '晴', '3级', '优'],
             ['周四', '16℃', '25℃', '阴', '2级', '良'],
             ['周五', '15℃', '24℃', '阴', '2级', '良'],
             ['周六', '15℃', '25℃', '晴', '3级', '优'],
             ['周日', '14℃,', '23℃', '小雨', '3级', '良']]
name=[lst_weather[i][0] for i in range (7)]
a=0
ls1=[]
for i in range(7):
    if lst_weather[i][5]=="优":
        a=a+1
        ls1.append(name[i])
ls1gai=",".join(str(i) for i in ls1)#去掉列表括号
print("空气质量为优的天数：{}".format(a),"，它们分别是：",ls1gai,sep="")

b=0
ls2=[]
for i in range(7):
    if eval(lst_weather[i][4][0])<3 and eval(lst_weather[i][2][0:2])<=25:
        b=b+1
        ls2.append(name[i])
ls2gai=",".join(str(i) for i in ls2)
print("风力低于3级且最高气温不超过25℃的天数：{}".format(b),"，它们分别是:",ls2gai,sep="")

c=0
ls3=[]
for i in range(7):
    if ((eval(lst_weather[i][1][0:2])+eval(lst_weather[i][2][0:2]))/2)<20:
        c=c+1
        ls3.append(name[i])
ls3gai=",".join(str(i) for i in ls3)       
print("平均气温低于20℃的天数：{}".format(c),"，它们分别是:",ls3gai,sep="")
