ls_score=[9,10,8,9,10,7,6,8,7,8]
ls_score.remove(max(ls_score))
ls_score.remove(min(ls_score))
print ("该参赛选手的最终得分：{}".format(sum(ls_score)/8))
