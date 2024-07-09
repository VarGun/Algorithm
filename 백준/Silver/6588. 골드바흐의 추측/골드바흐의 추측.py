import sys
input = sys.stdin.readline

def solution(num, arr):
  for i in range(3, num):
    if(arr[i] and arr[num - i]):
      print(f"{num} = {i} + {num - i}")
      return
  print("Goldbach's conjecture is wrong.")
  return


def is_prime_arr(num):
  # print('is_prime_arr num : ', num)
  arr = [True for i in range(num + 1)]
  # print(f"int(math.sqrt(num) + 1  : {int(math.sqrt(num) + 1 )}")
  for i in range(2, 1001):
    if arr[i] == True:
      j = 2
      while i * j <= num:
        # print(f"i : {i} / j : {j}")
        # print('arr[i * j] : ', arr[i * j])
        arr[i * j] = False
        j += 1
  # print(*arr)
  return arr
  
  
if __name__ == "__main__":
  num_list = []
  arr = is_prime_arr(1000000)
  while True:
    n = int(input())
    if n == 0 : break
    solution(n, arr)