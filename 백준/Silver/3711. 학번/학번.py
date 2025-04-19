T = int(input())
for _ in range(T):
    G = int(input())
    student_ids = [int(input()) for _ in range(G)]

    m = 1
    while True:
        remainders = set(sid % m for sid in student_ids)
        if len(remainders) == G:
            print(m)
            break
        m += 1
