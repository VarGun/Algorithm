from collections import defaultdict
def solution(clothes):
    gun = defaultdict(list)

    for name, category in clothes:
        gun[category].append(name)

    answer = 1
    for items in gun.values():
        answer *= (len(items) + 1)

    return answer - 1