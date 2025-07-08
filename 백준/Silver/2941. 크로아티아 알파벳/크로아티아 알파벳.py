arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

ans = len(s)

for e in arr:

    ans -= s.count(e)

print(ans)

