def distance(a,b,c,d):
    return ((a-c)**2+(b-d)**2)**0.5

d = int(input())
x,y = map(int, input().split())

if x >= 0 and y >= 0 and -x+d >= y:
    print(0)
else:
    if distance(x,y,0,0) <= distance(x,y,0,d) and distance(x,y,0,0) <= distance(x,y,d,0):
        print(1)
    elif distance(x,y,d,0) <=distance(x,y,0,d) and distance(x,y,d,0) <= distance(x,y,0,0):
        print(2)
    elif distance(x,y,0,d) <= distance(x,y,d,0) and distance(x,y,0,d) <= distance(x,y,0,0):
        print(3)

