import math

def calculate_intersections(x1, y1, r1, x2, y2, r2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # 두 원의 중심이 동일한 경우
    if x1 == x2 and y1 == y2:
        return -1 if r1 == r2 else 0
    
    # 두 원이 겹치는 경우
    if abs(r1 - r2) < dist < (r1 + r2):
        return 2
    elif dist == (r1 + r2) or dist == abs(r1 - r2):
        return 1
    else:
        return 0

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        result = calculate_intersections(x1, y1, r1, x2, y2, r2)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
