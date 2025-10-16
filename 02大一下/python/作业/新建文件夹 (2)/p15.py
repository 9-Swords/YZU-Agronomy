for i in range(1,1001):
    s=0
    for j in range(1,i):
        if i%j==0:
            s=s+j
    if s==i:
        print("{}=1".format(i),end="")
        for a in range(2,i):
            if i%a==0:
                print("+{}".format(a),end="")
        print()
