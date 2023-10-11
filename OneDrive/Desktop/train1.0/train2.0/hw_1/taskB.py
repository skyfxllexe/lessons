n, i, j = map(int, input().split())
if abs(i-j) == 1:
    print(0)
elif i < j:

    print(abs(min(j-i-1, i-1 + n - j)))
else:
    i,j = j,i
    print(abs(min(j-i-1, i-1 + n - j)))