import sys

s1 = input()
n = int(s1.split()[0])
m = int(s1.split()[1])
ans = 0

glist = []


nlist = []
for i in range(0,m):
    nlist.append(list(map(int,sys.stdin.readline().split())))


for i in range(0, n):
    glist.append(i)


def fp(a):
    if(glist[a] != a):
        return fp(glist[a])
    return a



ans = 0


for anscnt in range(0, m):
    n1 = nlist[anscnt][0]
    n2 = nlist[anscnt][1]
    num1 = fp(n1)
    num2 = fp(n2)
    if(num1 != num2):
        # glist[max(n1, n2)] = min(n1,n2)
        glist[max(num1, num2)] = min(num1,num2)
    elif(num1 == num2):
        ans = anscnt + 1
        break


print(ans)