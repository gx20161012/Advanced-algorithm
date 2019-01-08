def getNum(arr, num):
    if arr:
        qmax = list()
        qmin = list()
        i = 0
        j = 0
        res = 0
        length = len(arr)
        while i < length:
            while j < length:
                while qmin and arr[qmin[len(qmin)-1]] >= arr[j]:
                    qmin.pop()
                qmin.append(j)
                while qmax and arr[qmax[len(qmax)-1]] <= arr[j]:
                    qmax.pop()
                qmax.append(j)
                if arr[qmax[0]] - arr[qmin[0]] > num:
                    break
                j += 1
            if qmin[0] == i:
                qmin = qmin[1:]
            if qmax[0] == i:
                qmax = qmax[1:]
            res += j - i
            i += 1
        return res
arr = list(map(int, input().split(" ")))
num = int(input())
print(getNum(arr, num))