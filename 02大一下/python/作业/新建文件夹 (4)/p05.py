nums = [2, 7, 11, 15, 1, 8]
l1 = []
l =len(nums)               
for i in range(0, l-1) :
    for j in range(i+1,l):
        if nums[i] + nums[j] == 9:
            n = (nums[i], nums[j])
            l1.append(n)        
print(l1)
