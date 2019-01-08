def arraySort(length1, nums1, length2, nums2):
    '''
    '''
    nums3 = nums1.copy()
    nums1.clear()
    for i in range(length2):
        while nums2[i] in nums3:
            nums1.append(nums2[i])
            nums3.remove(nums2[i])
    if nums3:
        nums3 = sorted(nums3)
        nums1.extend(nums3)
    print(" ".join(str(num) for num in nums1))
T = int(input())
input_array = list()
for i in range(3*T):
    input_array.append(list(map(int, input().split(" "))))
for i in range(0, 3*T, 3):
    arraySort(input_array[i][0], input_array[i+1], input_array[i][1], input_array[i+2])