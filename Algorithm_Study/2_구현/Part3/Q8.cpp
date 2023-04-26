#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(){
    string str;
    cin >> str;
    string answer;
    int sum = 0;
    priority_queue<char, vector<char>, greater<char>> pq_c;

    for(int i = 0; i<str.size(); i++){
        if(str.at(i) - '0' >= 1 && str.at(i) -'0' <= 9){
            sum += (str.at(i) - '0');
            continue;
        }
        pq_c.push(str.at(i));
    }
    while(!pq_c.empty()){
        answer += pq_c.top();
        pq_c.pop();
    }
    answer += to_string(sum);
    cout << answer << endl;
    
}
