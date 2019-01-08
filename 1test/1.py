def getFrequencySort(length, nums):
    dict_num = dict()
    for i in range(length):
        if nums[i] in dict_num.keys():
            dict_num[nums[i]] += 1
        else:
            dict_num[nums[i]] = 1
    items = dict_num.items()
    backitems = [[v[1], v[0]] for v in items]
    backitems.sort()
    backitems.reverse()
    list_dict = []
    for i in range(0, len(backitems)):
        list_dict.append(backitems[i][1])
    nums.clear()
    i = 0
    while i < len(list_dict):
        k = i
        while i < len(list_dict)-1 and dict_num[list_dict[i]] == dict_num[list_dict[i+1]]:
            i += 1
        temp = list_dict[k:i+1]
        temp.sort()
        for j in temp:
            for u in range(dict_num[j]):
                nums.append(j)
        i += 1
    print(" ".join(str(num) for num in nums))
T = int(input())
input_array = list()
for i in range(2*T):
    input_array.append(list(map(int, input().split(" "))))
for i in range(0, 2*T, 2):
    getFrequencySort(input_array[i][0], input_array[i+1])