string = input()
w = input()

array = list(string.split(" "))
length = len(array)
w = int(w)
index = length - w + 1
sum = 0
for i in range(index):
    sum += int(max(array[i:i+w]))
print(sum)