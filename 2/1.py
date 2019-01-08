
def LCS(str1,str2,ls):
    length1=len(str1)
    length2=len(str2)
    ls_a=[]
    ls_b=[0]*(length2 + 1)
    for i in range(length1+1):
        temp=ls_b.copy()
        ls_a.append(temp)
    for i in range(1,length1 + 1):
        for j in range(1,length2 + 1):
            if str1[i-1]==str2[j-1]:
                ls_a[i][j]=ls_a[i-1][j-1] + 1
                ls[i][j]=0
            elif ls_a[i-1][j] > ls_a[i][j-1]:
                ls_a[i][j]=ls_a[i-1][j]
                ls[i][j]=1
            else:
                ls_a[i][j]=ls_a[i][j-1]
                ls[i][j]=-1
    return ls_a[length1][length2]

def PrintLCS(ls,str1,i,j):
    if i==0 or j==0:
        return
    if ls[i][j]==0:
        PrintLCS(ls,str1,i-1,j-1)
        print(str1[i-1],end="")
    elif ls[i][j] == 1:
        PrintLCS(ls,str1,i-1,j)
    else:
        PrintLCS(ls,str1,i,j-1)

s1=input().strip()
s2=input().strip()
length1=len(s1)
length2=len(s2)
lsa=[]
lsb = [None] * (length2 + 1)
for i in range(length1 + 1):
    temp=lsb.copy()
    lsa.append(temp)
len_res=LCS(s1,s2,lsa)
PrintLCS(lsa,s1,length1,length2)

