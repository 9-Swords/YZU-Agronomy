#输入密码进入系统
#有三次输入机会
passWord="YZU"
count=0
num=1
while count<3:
    mm=input("请输入密码：")
    if mm==passWord:
        print("密码正确，欢迎您进入系统！")
        continue
    else:
        if num<=2:
            print("密码不正确，请重新输入密码！")
            print("您还有",2-count,"次输入密码机会")
            num=num+1
        else:
            print("三次输入密码都不正确！！！")
            print("你不是本系统合法用户！")
        count=count+1
