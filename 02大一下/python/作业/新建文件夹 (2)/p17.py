a=input("请输入一行字符")
l=0
s=0
n=0
other=0
for i in a:
    if i>='A' and i<='Z' or i>='a' and i<='z':
        l=l+1
    elif i==' ':
        s=s+1
    elif i>='0' and i<='9':
        n=n+1
    else:
        other=other+1
print("英文字母",l,"个","空格",s,"个","数字",n,"个","其他字符",other,"个")
