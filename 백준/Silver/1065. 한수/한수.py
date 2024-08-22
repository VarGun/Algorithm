num = int(input())

def is_hansu(n):
    digits = list(map(int, str(n)))
    if n < 100:
        return True
    return digits[0] - digits[1] == digits[1] - digits[2]

hansu_count = sum(is_hansu(i) for i in range(1, num + 1))
print(hansu_count)
