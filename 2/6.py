while True:
    try:
        input_ls=list(map(int,input().strip().split()))
        count=input_ls[0]
        num_ls=input_ls[1:]
        res_temp=[]
        res=[]
        for i in range(count):
            num=0
            for j in range(count):
                if num_ls[i] > num_ls[j]:
                    num += 1
            res_temp.append(num)
        for i in range(count):
            temp=res_temp.index(min(res_temp))
            res_temp.pop(temp)
            res.append(num_ls.pop(temp))

        for k in range(count-1):
            print(res[k],end=" ")
        print(res[-1])
    except:
        break