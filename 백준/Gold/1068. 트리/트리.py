
n = int(input()) # 노드의 수
s = input().split() # 각 노드의 부모 노드 번호
m = int(input()) # 지울 노드 

cnt = 0

tr = [[] for i in range(0,n)] # 각 인덱스가 부모노드이고 인덱스에 해당하는 배열에 자식 노드의 번호를 저장

for i in range(0, n):
    if(s[i] != "-1"): # -1이 아니면 (부모가 있으면)
        tr[(int)(s[i])].append(i) # 부모노드 번호의 인덱스에 해당하는 배열에 자식 노드 번호 append

def search(a): # a = 지울 노드의 번호
    if(len(tr[a]) != 0): # 지울 노드의 자식을 담은 배열의 길이가 0이 아니면
        for i in tr[a]:
            search(i) # 자식이 없는 노드를 찾을 때 까지 재귀
    tr[a] = ["gun"] # 찾으면 지워진 노드로 표시

search(m)

for i in range(0, n):
    if (len(tr[i]) == 0): # 자식 노드가 없으면
        cnt += 1 # 리프노드의 수 + 1
    elif((tr[i][0]) != 'gun'): # 지워진 노드가 아니면서 자식을 담은 배열의 길이가 0이 아니면
        jud = 0 # 지워진 노드인지 판별할 수
        for j in tr[i]:
            if(len(tr[j]) == 1): # 배열의 길이가 1이면서
                if(tr[j][0] == 'gun'): # 지워진 노드로 표시되어 있으면
                    jud += 1 
        if(jud == len(tr[i])): # 자식들을 담은 배열의 길이 = 지워진 노드로 표시되어 있는 자식들의 수 
            cnt+=1 # 리프노드의 수 + 1

print(cnt)