array = [2008+4*i for i in range(-9,16)]

x,y,z = map(int, input().split())
if x == y:
    print(1)
elif x > 12 and y <= 12:
    print(1)
elif x <= 12 and y > 12:
    print(1)
else:
    print(0)