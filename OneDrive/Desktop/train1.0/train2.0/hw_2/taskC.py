s = input()


minim = 10e10
for i in range(1,len(s)):
    print(s+s[0:i])
    if s + s[0:i][::-1] == (s+s[0:i][::-1])[::-1]:
        minim = min(minim, len(s+s[0:i]))
print(minim)