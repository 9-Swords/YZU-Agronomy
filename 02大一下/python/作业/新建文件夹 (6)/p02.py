def f(a,b):
    s=0
    if b>=1916:
        s=(2*int(a[-1])+5)*50+1766-b
        return int(str(s)[-2]+str(s)[-1])
    else:
        return "本规则仅适用于计算100岁以内的人!"
a=input("请输入手机号：")
b=eval(input("请输入你出生年份："))
print(f(a,b))


