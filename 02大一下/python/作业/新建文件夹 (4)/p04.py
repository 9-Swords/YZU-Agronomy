a =[-3, 4, 7, 9, 13, 45, 67, 89, 100, 180]
print("a数组中的数据如下:")
for i in range(len(a)):
    print("{} " .format(a[i]),end=" ")
print()
m = int(input("请输入要查找的整数m，并按回车继续:"))
low=0
high=len(a)-1
while(low<=high):
    #**********FOUND**********
    mid=(low+high)//2
    if(m<a[mid]):
        high=mid-1
    #**********FOUND**********
    elif(m>a[mid]):
        low=mid+1
    else:
        k=mid
        break
else:
    k=-1
if(k>=0):
    print("m={},index={}".format(m,k))
else:
    print("没有找到！")   
