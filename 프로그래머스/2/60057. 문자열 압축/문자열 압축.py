def compress_string(s, tar_len, length): # 문자열, 압축할 길이, 원래 문자열 길이
    cur = ''
    cur_cnt = 0
    string = ''
    dic = {}
    for i in range(length // tar_len):
        tar_str = s[:tar_len]
        if(cur == ''):
            cur = tar_str
        elif(tar_str == cur):
            cur_cnt += 1
        elif(tar_str != cur):
            if(cur_cnt == 0):
                string += cur
            else:
                string += str(cur_cnt + 1) + cur
                cur_cnt = 0
            cur = tar_str
        s = s[tar_len:]
    
    if(cur_cnt != 0):
        string += str(cur_cnt + 1) + cur
    else:
        string += cur
    string += s
    
    return len(string)


def solution(s):
    answer = len(s)
    length = len(s)
    for l in range(1, length):
        answer = min(answer, compress_string(s, l, length))
    
    return answer