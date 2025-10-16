dic_zs={"面条":"12元","米饭":"1元","蛋炒饭":"15元","水饺":"9元"}
lst=[ eval(v[:v.index("元")]) for v in dic_zs.values()]
avg=sum(lst)/len(lst)
print("所有主食的平均价格为：{}元".format(avg))

lst2=[(eval(v[:v.index("元")]),k) for k,v in dic_zs.items()]
lst2.sort()
print("价格最高的主食名称为：{}".format(lst2[-1][1]))
