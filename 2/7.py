def portition(ls,low,high):
    temp=ls[low]
    while low < high:
        while low < high and ls[high] >= temp:
            high -= 1
        ls[low]=ls[high]
        while low < high and ls[low] <= temp:
            low += 1
        ls[high]=ls[low]
    ls[low]=temp
    return low

while True:
    try:
        input_ls=list(map(int,input().strip().split()))
        count=input_ls[0]
        num_ls=input_ls[1:]
        stack=[]
        stack.append(0)
        stack.append(count-1)
        while len(stack)>0:
            high=stack.pop()
            low=stack.pop()
            middle=portition(num_ls,low,high)
            if middle+1 < high:
                stack.append(middle+1)
                stack.append(high)
            if low < middle - 1:
                stack.append(low)
                stack.append(middle - 1)
        for k in range(count-1):
            print(num_ls[k],end=" ")
        print(num_ls[-1])
    except:
        break