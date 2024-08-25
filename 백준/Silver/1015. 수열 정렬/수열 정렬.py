A_size = int(input())
A = list(map(int, input().split()))

indexed_A = [(A[i], i) for i in range(A_size)]

indexed_A.sort()

P = [0] * A_size

for new_index in range(A_size):
    value, original_index = indexed_A[new_index]
    P[original_index] = new_index

print(' '.join(map(str, P)))
