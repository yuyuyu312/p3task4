list = []
n = int(input())

for x in range(n - 1):
    value = int(input())
    list.append(value)
list.sort()
k = 1
for i in list:
    if k == i:
        k = i + 1
print(k)
