dicTXL={"小新":["手机13913000001,qq18191220001"],
        "小亮":["手机13913000002,qq18191220002"],
        "小刚":["手机13913000003,qq18191220003"]}
dicother={"大刘":["手机13914000001,qq18191230001"],
          "大王":["手机13914000002,qq18191230002"],
          "大张":["手机13914000003,qq18191230003"]}
dicTXL.update(dicother)
dicWX={"小新":["微信xx9907"],"小刚":["微信gang1004"],
       "大王":["微信jack w"],"大刘":["微信liu666"]}
for k,v in dicWX.items():
    dicTXL[k]=dicTXL.get(k,0)+v
dicTXL["大王"][0]="手机13914000004,qq18191230002"
print(dicTXL)
name=input("请输入要查找人的姓名：")
if name in dicTXL:
    print(name,"的联系方式是：",dicTXL[name],sep="")
else:
    print("没有该同学的联系方式")
    
    
