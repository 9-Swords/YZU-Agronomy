dic_class={"托班":["爬爬班","跑跑班","跳跳班"],
           "小班":["绿芽班","红芽班"],
           "中班":["绿花班","红花班"],
           "大班":["绿果班","红果班"]}
dic_number={"爬爬班":26,"跑跑班":23,"跳跳班":25,
            "绿芽班":32,"红芽班":31,
            "绿花班":33,"红花班":34,
            "绿果班":32,"红果班":33}
for k in dic_class:
    s=0
    for x in dic_class[k]:
        if x in dic_number:
            s+=dic_number[x]
    print("{}：{}人".format(k,s))
print("全园：{}人".format(sum(dic_number.values())))

            
