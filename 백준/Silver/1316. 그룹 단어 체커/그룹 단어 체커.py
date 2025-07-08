def g(w):

    for i in range(len(w) - 1):

        if w[i] != w[i + 1] and w[i] in w[i + 1:]:

            return False

    return True

n = int(input())

words = [input() for _ in range(n)]

print(sum(1 for w in words if g(w)))

