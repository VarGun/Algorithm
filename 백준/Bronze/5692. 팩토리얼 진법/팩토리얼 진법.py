import sys

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

while True:
    num = sys.stdin.readline().strip()
    if num == "0":
        break

    n = len(num)
    result = sum(int(num[i]) * factorial(n - i) for i in range(n))
    print(result)
