def solution(prices):
    gun = [i for i in range(len(prices) - 1, -1, -1)]

    for i in range(len(prices) - 1):
        flag = False
        for j in range(i + 1, len(prices)):
            if(prices[i] > prices[j]):
                gun[i] = j - i
                break

    return gun