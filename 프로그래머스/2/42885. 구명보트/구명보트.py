from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
#     p = deque(people)
    
#     while p:
#         if(len(p) == 1):
#             answer += 1
#             break
#         if(p[0] + p[-1] <= limit):
#             answer += 1
#             p.pop()
#             p.popleft()
#         else:
#             answer += 1
#             p.pop()
    
    
    # end_idx = len(people) - 1
    s_idx = 0
    
    for i in range(len(people) - 1, - 1, -1):
        if(i == s_idx):
            answer += 1
            break
        elif(i < s_idx):
            break
        if(people[s_idx] + people[i] <= limit):
            answer += 1
            s_idx += 1
        else:
            answer += 1
    
    return answer