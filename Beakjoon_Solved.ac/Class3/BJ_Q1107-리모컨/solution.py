n = int(input())
m = int(input())
nlist = []
ans = 0
if(m == 0):
    ans1 = len(str(n))
    ans2 = ( n-100 if(n>=100) else 100-n)
    print(ans1 if(ans1<ans2) else ans2)
else:
    nlist = input().split(" ")
    if(n==100):
        print(0)
    elif(n>100):
        ans1 = n - 100
        ans2 = n + 100
        tmp = ans2
        for i in range(100, 1000000):
            jud = 0
            for j in nlist:
                if(j in str(i)):
                    jud = 1
                    break
            if(jud == 0):
                if(i<=n):
                    tmp = n - i + len(str(i))
                else:
                    tmp = i - n + len(str(i))
            if(tmp < ans2):
                ans2 = tmp
        ans = (ans1 if(ans1<ans2) else ans2)
        print(ans)
        
    else:
        ans1 = 100 - n # 100 에서 이동
        ans2 = 100 + n
        tmp = ans2
        cnt =0
        for i in range(0, 201):
            jud = 0
            for j in nlist:
                if(j in str(i)):
                    jud = 1 # 고장난 번호가 포함되어 있다면
                    break
                    
            if(jud == 0): # 고장난 번호가 포함되어 있지 않다면
                if(i>n):
                    tmp = len(str(i)) + i - n
                elif(i<n):
                    tmp = n - i +len(str(i))
                elif(i==n):
                    tmp = len(str(i))
            if(tmp < ans2):
                ans2 = tmp
                
                
        ans = (ans1 if(ans1<ans2) else ans2)
        print(ans)
            
    