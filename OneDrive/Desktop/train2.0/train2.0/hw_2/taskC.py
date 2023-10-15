s = input()
counter = 0


for i in range(len(s)//2):
    if s[i] != s[-1-i]:
        counter += 1
print(counter)