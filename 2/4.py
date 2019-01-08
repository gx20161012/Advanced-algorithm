while True:
    try:
        input_ls=list(map(int,input().strip().split()))
        count=input_ls[0]
        num_ls=input_ls[1:]
        num_ls.insert(0,0)
        for i in range(2,count+1):
            if num_ls[i] < num_ls[i-1]:
                num_ls[0]=num_ls[i]
                j=i-1
                while num_ls[j] > num_ls[0]:
                    num_ls[j+1]=num_ls[j]
                    j -= 1
                num_ls[j+1]=num_ls[0]
        num_ls.pop(0)
        for j in range(count-1):
            print(num_ls[j],end=" ")
        print(num_ls[-1])
    except:
        break