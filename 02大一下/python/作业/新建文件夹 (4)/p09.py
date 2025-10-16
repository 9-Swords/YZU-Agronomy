lst_busstop=["龙江新城市","阳光广场","汉江路","嫩江路","清凉山公园","拉萨路","五台山","莫愁路"]
a=input("请输入起始站：")
b=input("请输入终点站：")
c=lst_busstop.index(a)
d=lst_busstop.index(b)
if c<d:
    print("从{}前往{}需要{}站路".format(a,b,d-c))
else:
    print("您需要乘坐反方向线路")
