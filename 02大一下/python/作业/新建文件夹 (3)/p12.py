a=input("请输入金额：")
if "$" in a:
    b=round(eval(a[:-1])*6.6868,2)
    print(a[:-1],"美元可以兑换人民币",b,"元",sep="")
elif "￥" in a:
    b=round(eval(a[:-1])*0.1456,2)
    print(a[:-1],"元人民币可以兑换美元",b,"美元",sep="")
else:
    print("输入的为非法字符")

