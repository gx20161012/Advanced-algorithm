def f(a, b, c):
    k = 1
    while b > 0:
        if b % 2 == 1:
            k *= a
            k = k % c
        a = (a*a) % c
        b = b >> 1
    return k
n = int(input())
testcase = []
for i in range(n):
    testcase.append(list(map(int, input().split(" "))))
for i in range(n):
    print(f(testcase[i][0], testcase[i][1], testcase[i][2]))