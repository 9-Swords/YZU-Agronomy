#利用range()函数进行数值循环
#计算 1到100的整数和
result = 0   #保存累加结果的变量
for i in range(101):
    result+=i    #逐个获取从 1 到 100 这些值，并做累加操作
print("1到100的整数和为:", result)
