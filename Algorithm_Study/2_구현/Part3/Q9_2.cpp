#include <string>
#include <vector>
#include <iostream>
#include <string>
#include <queue>

using namespace std;

int makeSize(string str, int num){ // 문자열 압축 후 길이 반환, 압축할 문자열과 자를 단위를 입력인자로 받음
    queue<string> q;
    string ans; // 압축된 문자열
    for(int i = 0; i < str.size(); i += num){ // 주어진 단위 만큼 substr 하여 queue 에 push
        string ss = str.substr(i, num);
        q.push(str.substr(i,num));
    }
    int cnt = 1; // 특정 문자열이 반복되는 횟수
    string s1 = q.front(); // 검사할 문자열
    q.pop();
    while(!q.empty()){
        if(s1.compare(q.front()) == 0){ // 검사할 문자열이 queue의 최상단의 원소와 같을 경우
            q.pop(); // 다음 원소를 확인하기 위해 pop
            cnt += 1; // 반복 횟수 증가
        }
        else{ // 검사할 문자열이 queue 의 최상단의 원소와 다를 경우
            if(cnt != 1){ // cnt 가 1이 아닐 경우 ans(압축된 문자열)에 횟수 추가
                ans += to_string(cnt);
            }
            ans += s1; // 반복된 문자열 추가
            s1 = q.front(); // 검사할 문자열 교체
            q.pop(); // 다음 원소를 확인하기 위해 pop
            cnt = 1; // 반복된 횟수 초기화
        }
    }
    if(cnt != 1){ // queue 검사가 끝난 후 마찬가지로 cnt와 검사할 문자열을 ans(압축된 문자열) 에 추가
        ans += to_string(cnt);
    }
    ans += s1;
    return ans.size(); // 압축된 문자열의 길이 반환
}

int solution(string s){
    int len = s.size();
    int answer = len; // 압축하지 않은 문자열의 길이
    for(int i = 1; i< len; i++){ // 길이 내에서 모든 숫자를 반복하며 최솟값 찾기
        int result = makeSize(s, i);
        if(answer > result){
            answer = result;
        }
    }
    return answer;
}
int main(){
    string s;
    cin >> s;
    cout << solution(s)<<endl;
}