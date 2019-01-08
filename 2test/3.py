def sum(arr, frm, to):  
    total = 0
    for i in range(frm, to + 1): 
        total += arr[i] 
    return total 
def findmax(arr,n,k):
    ls_n=[0]*(n+1)
    ls_k=[]
    for i in range(k+1):
        temp=ls_n.copy()
        ls_k.append(temp)
    for i in range(1,n+1):
        ls_k[1][i]=sum(arr,0,i-1)
    for i in range(1,k+1):
        ls_k[i][1]=arr[0]
    for i in range(2,k+1):
        for j in range(2,n+1):
            best = 100000000
            for p in range(1,j+1):
                best=min(best,max(ls_k[i-1][p],sum(arr,p,j-1)))
            ls_k[i][j]=best
    return ls_k[k][n]

count=int(input().strip())
k,n,arr=[],[],[]
for i in range(count):
    num_ls=list(map(int,input().strip().split()))
    k.append(num_ls[0])
    n.append(num_ls[1])
    arr.append(list(map(int,input().strip().split())))

for j in range(count):
    print(findmax(arr[j], n[j], k[j]))
    