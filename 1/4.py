n = int(input())
sum = 2
if n >= 1:
    if n == 1:
        print(sum)
    else:
        for i in range(2, n+1):
            sum += 2 * pow(3, i -1)
        print(sum)