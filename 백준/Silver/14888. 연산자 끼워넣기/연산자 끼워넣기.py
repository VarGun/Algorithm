N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

_min = 1000000000 + 1
_max = _min * (-1)


def backT(num, ops, depth):
  global _max, _min, nums, N
  if (depth == N - 1):
    if (num < _min):
      _min = num
    if (num > _max):
      _max = num
    return
  for i in range(4):
    if (ops[i] != 0):
      ops[i] -= 1
      if (i == 0):
        backT(num + nums[depth + 1], ops, depth + 1)
      elif (i == 1):
        backT(num - nums[depth + 1], ops, depth + 1)
      elif (i == 2):
        backT(num * nums[depth + 1], ops, depth + 1)
      else:
        if (num < 0):
          gun = abs(num)
          gun = gun // nums[depth + 1]
          backT(gun * (-1), ops, depth + 1)
        else:
          backT(num // nums[depth + 1], ops, depth + 1)
      ops[i] += 1


backT(nums[0], ops, 0)
print(_max)
print(_min)
