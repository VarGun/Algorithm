def get_rank(s):
    total = 0
    for i in range(1, len(s)):
        total += 26 ** i
    val = 0
    for i in range(len(s)):
        val = val * 26 + (ord(s[i]) - 97)
    return total + val + 1 # 순위가 1부터 시작하니까

def get_word(n):
    length = 1
    while n > 26 ** length:
        n -= 26 ** length
        length += 1
    n -= 1 # 순위가 1부터 시작했으니까
    word = ""
    for _ in range(length):
        word += chr(97 + n % 26)
        n //= 26
    return word[::-1]


def solution(n, bans):
    answer = ''
    bans.sort(key = lambda x : (len(x), x))
    cnt = 0 # 지울 단어 수 (bans 에서 n 보다 순위가 낮은 애들 수)
    for b in bans:
        if(get_rank(b) > n + cnt): # 밀릴 수 있으니까
            break
        cnt += 1

    return get_word(n + cnt)