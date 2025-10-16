worddic=dict()
while True:
    print("请选择功能：\n1: 输入\n2：查找\n3：退出")
    c=input("请输入对应序号：")
    if c=="1":
        while True:
            word=input("请输入英文单词（直接按回车结束输入）：")
            #**********FOUND**********
            if len(word)==0: break
            meaning=input("请输入中文翻译：")
            worddic[word]=meaning
            print("该单词已添加到字典库。")
    elif c=="2":
        #**********FOUND**********
        while True:
            word=input("请输入要查询的英文单词（直接按回车结束查询）：")
            if len(word)==0: break
            #**********FOUND**********
            if word in worddic:
                print("{}的中文翻译是:{}".format(word,worddic[word]))
            else:
                print("字典库中未找到这个单词")
    elif c=="3":
        break
    else:
        print("输入有误！")    
