## Set와 BufferedReader
----------
## Set
#### Set는 중복된 값을 가질 수 없음 (장점이자 단점)
### 선언

    HashSet<타입> Set명 = new HashSet<타입>();

#### 추가적으로 LinkedSet, TreeSet이 있음
#### LinkedSet : 중복은 없으나 순서는 있음 (add 한 순서대로 값 저장)
#### TreeSet : 오름차순으로 값을 정렬해 저장함. 다른 Set들에 비해 검색시 속도가 매우 빠름.


### 추가

    Set명.add("값");


### 제거

    Set명.remove("값");


### 비우기

    Set명.clear();


### 크기
    Set명.size();


### 출력
+ 출력 위해 Iterator안에 담기
    Iterator<타입> iterator명 = Set명.Iterator();
+ Iterator 안에 담은 내용 출력하기
    Iterator명.next();
    or
    while(iterator명.hasNext()) {
    iterator명.next(); // 값 없을때까지 계속 출력
    }

----------
## BufferedReader

### Buffer
#### 버퍼(buffer) : 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 임시 메모리 영역
#### 입출력 속도 향상을 위해 사용

### 버퍼를 이용한 입력 : BufferedReader
#### 사용시 예외처리 혹은 throwsIOException 필수

### 버퍼를 이용한 출력 : BufferedWriter

### Scanner와 BufferedReader
#### Scanner는 띄어쓰기(Space)와 개행문자(Enter)를 경계로 입력값을 인식함.
#### BufferedReader는 엔터만 경계로 인식하고 입력값을 모두 String형태로 인식함 (-> 필요시 가공이 필수)
#### 하지만 BufferedReader의 속도가 상대적으로 빠름.

### BufferedReader 선언
#### 콘솔에서 입력 받을 경우

    BufferedReader 버퍼리더변수명 = new BufferedReader(new InputStreamReader(System.in));

#### 파일에서 입력 받을 경우

    FileReader 파일리더변수명 = new FileReader("파일명");
    BufferedReader 버퍼리더명 = new BufferedReader(파일리더변수명);

#### 형변환

    int 변수명 = Integer.parseInt(버퍼리터변수명.readLine());
    버퍼리더명.close();


### BufferedWriter 선언

    BufferedWriter 버퍼리더변수명 = new BufferedWriter(new FileWriter("파일명));
    
#### 출력

    버퍼리더명.write("값);

#### 개행

    버퍼리더명.nextLine();

#### 남아있는 데이터 모두 출력

    버퍼리더명.flush();

----------

### Point
#### 시간초과 때문에 몇시간이나 낭비했다 다음부터는 Scanner보다 Buffer를 더 사용해볼 생각
