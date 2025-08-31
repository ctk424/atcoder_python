x, y = map(int, input().split())
for _ in range(2, 10):
    c = x + y
    c = str(c)
    c = c[::-1]
    c = int(c)
    # print(c)
    x = y
    y = c
print(y)
