

def solution(players, m, k):
    ans = 0
    dp = [0 for _ in range(24)] # 서버 수
    for i in range(24):
        
        if(players[i] >= (dp[i] + 1) * m):
            tar = players[i] // m # 필요한 서버 수
            need = tar - dp[i]
            ans += need
            for j in range(i, i + k):
                if(j < 24):
                    dp[j] += need
                    
        

    return ans