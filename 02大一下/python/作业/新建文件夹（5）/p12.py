dic_repertory={"酱油":50,"醋":60,"盐":100,"糖":120,"鸡精":20,"麻油":40}
dic_change={"酱油":100,"醋":80,"鸡精":50,"蚝油":60}
for k,v in dic_change.items():
    dic_repertory[k]=v
print(dic_repertory)
c=[(v,k) for k,v in dic_repertory.items()]
c.sort(reverse=True)
for x in c:
    print(x[1],x[0],sep=":")
print("库存数量最多的商品为{},数量为{}".format(c[0][1],c[0][0]))
print("库存数量最少的商品为{},数量为{}".format(c[-1][1],c[-1][0]))

