def getReverseNum(length, nums):
    count = 0
    for i in range(length-1):
        for j in range(i+1, length):
            if nums[i] > nums[j]:
                count += 1
    return count
T = int(input())
input_array = list()
for i in range(2*T):
    input_array.append(list(map(int, input().split(" "))))
for i in range(0, 2*T, 2):
    print(getReverseNum(input_array[i][0], input_array[i+1]))
