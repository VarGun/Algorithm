def convert_sec(time): # time / 'HH:MM:SS'
    time_tmp = list(map(int, time.split(':')))
    time_sec = time_tmp[0] * 60 * 60 + time_tmp[1] * 60 + time_tmp[2]
    return time_sec

def format_str(num):
    return str(num).zfill(2)
    

def convert_time(sec): # sec / 6809
    sec_h = str(sec // (60 * 60)).zfill(2)
    sec = sec % (60 * 60)
    sec_m = sec // 60
    sec = sec % 60
    formatted = list(map(format_str, [sec_h, sec_m, sec]))
    return (':').join(formatted)


def solution(play_time, adv_time, logs):
    answer = '00:00:00'
    # play_time : 영상 길기, adv_time : 광고 영상 길이, logs : 시청자들이 본 구간
    
    play_sec = convert_sec(play_time)
    adv_sec = convert_sec(adv_time)
    if(play_sec == adv_sec ):
        return answer
    
    timeline = [0 for _ in range(play_sec + 1)] # 각 시간 별 시청 횟수 / 초 단위
    
    for log in logs: # 각 시작 시간, 끝나는 시간 처리
        start, end = log.split('-')
        timeline[convert_sec(start)] += 1 # 시작 시간 + 1
        timeline[convert_sec(end)] -= 1 # 끝나는 시간 - 1
    # 이 시점에서 timeline : 각 시간마다 들어오고 나간 시청자 수 총합
    
    for i in range(1, len(timeline)): # 0 부터 시작하면 인덱스 오류
        timeline[i] += timeline[i - 1] # 각 구간 채우기 -> 그 시간대에 보고 있는 시청자 수
    # 이 시점에서 timeline : 그 시간대에 보고 있는 시청자 수
    
    timeline[0] = 0
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i - 1]
    
    
    max_sum = timeline[adv_sec] # 0초 부터 광고 길이 만큼
    max_start = 0

    for i in range(1, play_sec): # s는 'dp[end]-dp[start]'에서 start 역할
        if (i + adv_sec >= play_sec):
            end = play_sec
        else:
            end = i + adv_sec
        cur = timeline[end] - timeline[i]  # [s+1, end] 구간합

        if cur > max_sum:
            max_sum = cur
            max_start = i + 1

    
    
    return convert_time(max_start)