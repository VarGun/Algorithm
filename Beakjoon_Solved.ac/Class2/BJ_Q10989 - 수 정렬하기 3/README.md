# [ 수 정렬하기 3 ](https://www.acmicpc.net/problem/10989)  BAEKJOON : Q.10989

### 문제
#### N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
----------
### 입력
#### 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
----------
### 출력
#### 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
----------
### 예제 입력 1

    10
    5
    2
    3
    1
    4
    2
    3
    5
    1
    7

----------
### 예제 출력 1

    1
    1
    2
    2
    3
    3
    4
    5
    5
    7

----------
### Point
#### ArrayList로 수를 받고 정렬(Collections.sort(list))했을 때는 메모리 초과가 떠서 혹시나 싶은 마음에 배열을 사용(Arrays.sort())했더니 해결됐다 -> 배열이 List보다 정렬 메소드에 한해서는 메모리 관리에 용이함.