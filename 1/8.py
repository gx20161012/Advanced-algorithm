def change(llist, rlist):
    r = lenth - 1
    tflag = 1
    global flag
    global cha
    while r >= 0 and tflag:
        for l in range(lenth):
            if ((rlist[r] - llist[l]) * 2 <= cha and rlist[r] > llist[l]):
                rlist[r], llist[l] = llist[l], rlist[r]
                rlist.sort()
                llist.sort()
                cha = sum(rlist) - sum(llist)
                tflag = 0
                break
        else:
            r -= 1
    if (r < 0):
        flag = 0
    return (llist, rlist)

li1 = list(map(int,input().split(" ")))
li2 = list(map(int,input().split(" ")))
sourcelist=[]
for i in li1:
    sourcelist.append(i)
for j in li2:
    sourcelist.append(j)
sourcelist.sort()
lenth = len(sourcelist) // 2
llist = sourcelist[:lenth]
rlist = sourcelist[lenth:]
cha = sum(rlist) - sum(llist)
flag = 1
while flag:
    (llist, rlist) = change(llist, rlist)
print(cha)