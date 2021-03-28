a = int(input())
y = 0

while a <= 700000:
    ren = a * 7.1 / 100
    a += ren
    y += 1

if y == 0:
    y += 1

print(y)
