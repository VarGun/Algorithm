while True:
    N = int(input())
    if N == 0:
        break

    students = []
    max_height = -1.0

    for _ in range(N):
        name, height = input().split()
        height = float(height)
        students.append((name, height))
        if height > max_height:
            max_height = height

    result = [name for name, height in students if height == max_height]
    print(' '.join(result))
