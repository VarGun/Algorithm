#include <string>
#include <vector>
#include <iostream>
#include <string>
#include <queue>

using namespace std;

int makeSize(string str, int num){
    queue<string> q;
    string ans;
    for(int i = 0; i < str.size(); i+=num){
        string ss = str.substr(i, num);
        q.push(ss);
    }
    int cnt = 1;
    string s1 = q.front();
    q.pop();
    while(!q.empty()){
        if(s1.compare(q.front()) == 0){
            q.pop();
            cnt += 1;
        }
        else{
            if(cnt != 1){
                ans += to_string(cnt);
            }
            ans += s1;
            s1 = q.front();
            q.pop();
            cnt = 1;
        }
    }
    if(cnt != 1){
        ans += to_string(cnt);
    }
    ans += s1;
    return ans.size();
}

int solution(string s){
    int len = s.size();
    int answer = len;
    for(int i = 1; i< len; i++){
        int result = makeSize(s, i);
        if(answer > result){
            answer = result;
        }
    }
    return answer;
}