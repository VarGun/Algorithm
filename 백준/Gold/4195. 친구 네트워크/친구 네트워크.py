import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline
n = int(input())


def fp(a): # find parent
    if(tr.get(a)[0] != a): # 자신의 이름과 부모의 이름이 같지 않을 때 ( 자신이 루트 노드가 아닐 때 )
        tr.get(a)[0] = fp(tr.get(a)[0]) # 부모 노드를 바꾸면서 재귀
        return tr.get(a)[0]
    
    return a
   

al2 = []

for i in range(0, n):
    m = int(input())
    tr = {} # 이름, 부모, network 수를 저장할 딕셔너리
    for j in range(0, m):
        st = input()
        f1 = st.split()[0] # 첫번째 친구
        f2 = st.split()[1] # 두번째 친구
        
        if (f1 not in tr):
            if (f2 not in tr): # 둘 다 처음 입력되는 값인 경우
                tr[f1] = [f2, 1] # 첫번째 친구의 부모를 두번째 친구로 설정 / 초기 network 값 : 1
                tr[f2] = [f2, 2] # 두번째 친구의 부모로 설정 / 초기 입력 network 값 : 2 ( f1 network + f2 network )
                print(2)
            else: # f2 만 입력되어 있는 값인 경우
                st2 = fp(f2) # f2의 부모 호출
                net = tr[st2][1] # f2부모 network 값
                tr[f1] = [st2, 1] # f1 : 부모 = f2의 부모, network = 1 로 설정해서 딕셔너리에 추가
                tr[st2][1] = net + 1 # 부모의 network 값 + 1
                print(net + 1)
                
        else:
            if(f2 not in tr): # f1 만 입력되어 있는 값인 경우
                st1 = fp(f1) # f1의 부모 호출
                net = tr[st1][1] # f1의 부모 network 값
                tr[f2] = [st1, 1] # f2 : 부모 = f2의 부모, network = 1 로 설정해서 딕셔너리에 추가
                tr[st1][1] = net + 1 # 부모의 network 값 + 1
                print(net+1)
            else:
                st1 = fp(f1) # f1의 부모 호출
                st2 = fp(f2) # f2의 부모 호출
                
                if(st1 != st2): # f1과 f2의 부모가 다른 경우
                    net = tr[st2][1] # f1의 부모 network 값
                    net2 = tr[st1][1] # f2의 부모 network 값
                    
                    tr[st1][0] = st2 # f1의 부모의 부모를 f2 의 부모로 설정
                    tr[st2][1] = net+net2 # f2의 부모의 network 값에 f1 의 부모의 network 값 더함.
                    print(net+net2)
                else: # 부모가 같은 경우
                    print(tr[st1][1]) # f1의 부모 network 값 출력 
