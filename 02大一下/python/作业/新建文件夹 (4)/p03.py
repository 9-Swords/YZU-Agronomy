N = 5
stu = []
for i in range(N):
    stu.append(['','',[]])
for i in range(N):
    stu[i][0] = input("请输入第{}个学生学号: ".format(i+1))
    stu[i][1] = input("请输入第{}个学生姓名: ".format(i+1))
    for j in range(3):            
        #**********FOUND**********
        stu[i][2].append(input("请输入第{}个成绩: ".format(j + 1)))
#**********FOUND**********
for i in range(N):
    print('{:<6}  {:<10}'.format(stu[i][0],stu[i][1] ),end="")
    for j in range(3):            
        #**********FOUND**********
        print('{:<4d}'.format(stu[i][2][j]),end="  ")
    print()
