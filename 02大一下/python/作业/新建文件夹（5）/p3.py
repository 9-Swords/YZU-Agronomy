s=input("请输入一个英文字符串：")
dict1={}
for ch in s:
    dict1[ch]=dict1.get(ch,0)+1
list1=[k for k,v in dict1.items() if v==1]
print(list1)
