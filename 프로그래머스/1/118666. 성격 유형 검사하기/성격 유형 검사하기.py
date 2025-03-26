def solution(s, c):
    ans = ''
    d = {
        'R' : 0, 'T' : 0,
        'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0,
        'A' : 0, 'N' : 0
    }
    for i in range(len(s)):
        # print(c[i])
        if(c[i] > 4):
            d[s[i][1]] += c[i] - 4
        elif(c[i] < 4):
            d[s[i][0]] += 4 - c[i]
    
    if(d['R'] >= d['T']):
        ans += 'R'
    else:
        ans += 'T'
    
    if(d['C'] >= d['F']):
        ans += 'C'
    else:
        ans += 'F'
    
    if(d['J'] >= d['M']):
        ans += 'J'
    else:
        ans += 'M'
        
    if(d['A'] >= d['N']):
        ans += 'A'
    else:
        ans += 'N'
    
    return ans