dic_score={"李刚":93,"陈静":78,"张金柱":88,"黄宁":83,"赵启山":91,"李欣":65,"张翔飞":72,"孙梅":79}
d=[(v,k) for k,v in dic_score.items()]
d.sort(reverse=True)
for x in d:
    print(x[1])
