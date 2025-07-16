answer = 0
def backT(num, depth, target, numbers, gun):
    global answer
    if(depth == len(numbers)):
        if(num == target):
            answer += 1
        return
    tmp = num + numbers[depth]
    gun.append(tmp)
    backT(tmp, depth + 1, target, numbers, gun)
    gun.pop()
    tmp = num - numbers[depth]
    gun.append(-1 * tmp)
    backT(tmp, depth + 1, target, numbers, gun)
    gun.pop()
    

def solution(numbers, target):
    gun = [numbers[0]]
    backT(numbers[0], 1, target, numbers, gun)
    gun = [-1 * numbers[0]]
    
    backT(-1 * numbers[0], 1, target, numbers, gun)
    
    return answer