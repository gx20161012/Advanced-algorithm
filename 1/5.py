def getKmin(nums, left, right, k):
    '''
    '''
    list_range = nums[left:right]
    list_range.sort()
    list_range.reverse()
    return list_range[k-1]
nums = list(map(int, input().split(" ")))
arrange = list(map(int, input().split(" ")))
k = int(input())
print(getKmin(nums, arrange[0], arrange[1], k))