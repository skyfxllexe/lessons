a = int(input())
b = int(input())
c = int(input())
d = int(input())


if a == 0 and b == 0 and (c!=0 or d != 0):
    print('INF')
if (a == c and b == d) or a == 0 or (a/c==b/d):
    print('NO')
else:
    if (-b/a == -b//a):
        print(-b//a)
    else:
        print('NO')
