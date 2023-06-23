tem = [i for i in range(1, 10000)]
for i in range(1, 10000):
    test = i
    for j in str(i):
        test += int(j)
    if test in tem:
        tem.remove(test)

for m in tem:
    print(m)