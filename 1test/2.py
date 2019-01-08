def getMinSwap(length, nums):
    dict_num = dict()
    sortedNums = list(nums)
    sortedNums.sort()
    for i in range(0, length):
        dict_num[sortedNums[i]] = i
    count = 0
    for i in range(length):
        while nums[i] != sortedNums[i]:
            temp = nums[i]
            index = dict_num[nums[i]]
            nums[i] = nums[index]
            nums[index] = temp
            count += 1
    return count
n = int(input())
input_array = list()
for i in range(2*n):
    nums = list(map(int, input().split(" ")))
    input_array.append(nums)
for i in range(0, 2*n, 2):
    print(getMinSwap(input_array[i][0], input_array[i+1]))