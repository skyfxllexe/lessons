array = list(map(int, input().split()))

maxim_dist = 0

shops = []
houses = []
for i,j in enumerate(array):
    if j == 1:
        houses.append(i)
    if j == 2:
        shops.append(i)
min_max_dist = 0
for i in range(len(houses)):
    
    min_dist = abs(houses[i]-shops[0])
    for j in range(len(shops)):
        if abs(houses[i]-shops[j]) < min_dist:
            min_dist = abs(houses[i]-shops[j])
    if min_dist > min_max_dist:
        min_max_dist = min_dist

print(min_max_dist)
