while True:
    try:
        input_ls=list(map(int,input().strip().split()))
        count=input_ls[0]
        num_ls=input_ls[1:]
        for i in range(count):
            for j in range(count-i-1):
                if num_ls[j]>num_ls[j+1]:
                    num_ls[j],num_ls[j+1]=num_ls[j+1],num_ls[j]
        for k in range(count-1):
            print(num_ls[k],end=" ")
        print(num_ls[-1])
    except:
        break