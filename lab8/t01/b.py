a1, a2 = 1, 1
s1 = 3
s2 = 12
n = int(input('член послідовності: '))
for x in range(3, n+1):
    ak = a2 / x + a1
    s2 += 3 ** x / ak
    a1, a2 = a2, ak

print(s2)
