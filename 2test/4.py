from math import sqrt
def g(n):
    lim = int(sqrt(n))
    a = [0] * (lim-2)
    for i in range(lim-2):
        if a[i] == 0:
            j = i + 2
            k = 2
            while k*j < lim:
                a[k*j-2] = 1
                k += 1
    c = 0
    for i in range(0, lim-2):
        if a[i] == 0:
            if pow(i+2, 8) <= n:
                c += 1
            for j in range(i+1, lim-2):
                if a[j] == 0:
                    if pow((i+2)*(j+2), 2) <= n:
                        c += 1
                    else:
                        break
    return c      
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
for i in range(n):
    print(g(array[i]))