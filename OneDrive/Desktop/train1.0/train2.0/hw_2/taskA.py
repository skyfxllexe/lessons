

arr = []
while True:
    num =int(input())
    if num == 0:
        break
    arr.append(num)
count = 0
maxim = max(arr)
for i in range(len(arr)):
    if arr[i] == maxim:
        count += 1
print(count)