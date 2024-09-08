S = input()
count = sum(1 for i in range(len(S)-1) if S[i] != S[i+1])
print((count + 1) // 2)