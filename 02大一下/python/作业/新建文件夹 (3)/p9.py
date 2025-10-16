s="JanFebMarAprMayJunJulAugSepOctNovDec"
a=eval(input("请输入月份数字（1-12）："))
print(a,"月对应的英文缩写是：",s[(a-1)*3:a*3])
