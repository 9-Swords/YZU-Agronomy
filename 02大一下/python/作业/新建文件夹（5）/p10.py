d={"Jack":"654321","Tom":"t_1_o_2_m","Karry":"k888888"}
y=input("请输入用户名：")
if y in d:
    mima=input("请输入密码：")
    if mima==d.get(y):
        print("登录成功！")
    else:
        print("密码不正确！")
else:
    print("用户名不正确！")
    
        
