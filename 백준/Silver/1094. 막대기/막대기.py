x = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
count = 0

for length in stick:
    if x == 0:
        break
    if x >= length:
        count += 1
        x -= length

print(count)
