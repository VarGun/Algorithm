def solution(b, y):
    answer = []
    gun = []
    total = b + y
    for i in range(1, total):
        if(total % i == 0 and (i - 2) * (total // i - 2) == y) :
            answer = [i, total // i]
            

    print('gun : ', gun)
    return answer