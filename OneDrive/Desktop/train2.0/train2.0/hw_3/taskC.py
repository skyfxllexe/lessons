arr = list(map(int, input().split()))
set1 = set() # все
set2 = set() # не уникальные

for i in range(len(arr)):
    if arr[i] not in set1:
        set1.add(arr[i])
    else:
        set2.add(arr[i])
print(set1.difference(set2))
