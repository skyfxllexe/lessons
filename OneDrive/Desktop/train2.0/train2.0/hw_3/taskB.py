arr = list(map(int, input().split()))

mySet = set()
for i in range(len(arr)):
    l = len(mySet)
    mySet.add(arr[i])
    if len(mySet) == l:
        print('YES')
        print(mySet)
    else:
        print('NO')
        print(mySet)