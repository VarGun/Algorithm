def solution(n, k, cmd):
    table = {}
    answer = ['O'] * n
    d_stack = []
    for i in range(n):
        table[i] = [i - 1, i + 1]
    for c in cmd:
        if(len(c) == 1): # C or Z
            if(c == 'C'):
                answer[k] = 'X'
                pre, nxt = table[k]
                d_stack.append((pre, nxt, k))
                
                if(pre == -1):
                    table[nxt][0] = pre
                    k = nxt
                elif(nxt == n):
                    table[pre][1] = nxt
                    k = pre
                else:
                    table[pre][1] = nxt
                    table[nxt][0] = pre
                    k = nxt                  
                
            else: # Z
                pre, nxt, cur = d_stack.pop()

                if(pre == -1):
                    table[nxt][0] = cur
                elif(nxt == n):
                    table[pre][1] = cur
                else:
                    table[pre][1] = cur
                    table[nxt][0] = cur
                answer[cur] = 'O'
        
        else: # U or D
            com, num = c.split(" ")
            num = int(num)
            if com == 'U':
                for _ in range(num):
                    k = table[k][0]
            else:
                for _ in range(num):
                    k = table[k][1]
    
    return ''.join(answer)