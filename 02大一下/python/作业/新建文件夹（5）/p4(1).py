dic_zs1={}
while True:
    name=input("请输入主食名称：")
    jg=input("请输入主食价格(元)：")
    jg=eval(jg[:jg.index("元")]) if "元" in jg else eval(jg)
    dic_zs1[name]=jg
    jx=input("数据已存入，是否继续？(Y/N)")
    if jx=="n" or jx=="N" :break
lst=[v for v in dic_zs.values()]
avg=sum(lst)/len(lst)
print("所有主食的平均价格为：{}元".format(avg))

lst2=[(v,k) for k,v in dic_zs.items()]
lst2.sort()
print("价格最高的主食名称为：{}".format(lst2[-1][1]))
