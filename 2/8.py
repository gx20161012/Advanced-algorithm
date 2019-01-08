# def merge(sls,tls,i,m,n):
#     k=i
#     j=m+1
#     while i<=m and j<=n:
#         if sls[i] < tls[j]:
#             tls[k]=sls[i]
#             i += 1
#         else:
#             tls[k]=sls[j]
#             j += 1
#         k += 1
#     if i <= m:
#         for l in range(m-i+1):
#             tls[k+l]=sls[i+l]
#     if j <= n:
#         for l in range(n-j+1):
#             tls[k+l]=sls[j+l]
#
# def MergePass(sls,tls,s,n):
#     i=1
#     while i <= n-2*s+1:
#         merge(sls,tls,i,i+s-1,i+2*s-1)
#         i=i+2*s
#     if i<n-s+1:
#         merge(sls,tls,i,i+s-1,n)
#     else:
#         j=i
#         while j <=n:
#             tls[j]=sls[j]
#             j+= 1
#
# def MergeSort(ls):
#     count=len(ls)
#     tr=[None]*count
#     k=1
#     while k<count:
#         MergePass(ls,tr,k,count)
#         k=2*k
#         MergePass(tr,ls,k,count)
#         k=2*k
#     print(tr)
#
# while True:
#     try:
#         input_ls=list(map(int,input().strip().split()))
#         count=input_ls[0]
#         num_ls=input_ls[1:]
#         MergeSort(num_ls)
#         # for k in range(count-1):
#         #     print(num_ls[k],end=" ")
#         # print(num_ls[-1])
#     except:
#         break

def merge(seq,low,mid,height):

    left = seq[low:mid]
    right = seq[mid:height]

    k = 0
    j = 0
    result = []

    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[j])
            j += 1

    result += left[k:]
    result += right[j:]
    seq[low:height] = result
    return seq



def mergesort(seq):
    i = 1
    while i < len(seq):
        low = 0
        while low < len(seq):
            mid = low + i
            height = min(low + 2 * i, len(seq))
            if mid < height:
                res=merge(seq,low,mid,height)
            low += 2*i
        i *= 2
    return res
def print_ls_str(ls):
    length=len(ls)
    for i in range(length-1):
        print(ls[i],end=" ")
    print(ls[-1])
while True:
    try:
        input_ls=list(map(int,input().strip().split()))
        num=input_ls[0]
        num_ls=input_ls[1:]
        print_ls_str(mergesort(num_ls))
    except:
        break
