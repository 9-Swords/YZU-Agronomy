def judge(password):
    s=0
    for i in password:
        if i>="0" and i<="9":
            s+=1
            break
        else:
            continue
    for i in password:
        if i>="a" and i<="z":
            s+=1
            break
        else:
            continue
    for i in password:
        if i>="A" and i<="Z":
            s+=1
            break
        else:
            continue
    if len(password)>=8:
            s+=1
    return s
password=input("请输入测试密码：")
print("{}的密码强度为{}级".format(password,judge(password)))
        
    
