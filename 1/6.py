array = input().split(" ")
target = int(input())
array = list(map(int, array))
array = sorted(array)
left = 0
right = len(array) - 1
count = 0
while left < right:
    if array[left] + array[right] == target:
        count += 1
        left += 1
        right -= 1
    elif array[left] + array[right] < target:
        left += 1
    else:
        right -= 1
print(count)
print(array, target)