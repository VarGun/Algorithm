import sys

L = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())

nums.sort()

if n in nums:
    print(0)
else:
    min_val, max_val = 0, 0
    
    for num in nums:
        if num < n:
            min_val = num
        elif num > n and max_val == 0:
            max_val = num

    max_val -= 1  
    min_val += 1
    
    result = (n - min_val) * (max_val - n + 1) + (max_val - n)
    print(result)
