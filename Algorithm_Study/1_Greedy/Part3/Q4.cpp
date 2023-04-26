#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n;
    vector<int> v;
    cin >> n;
    for(int i = 0; i < n; i++){
        int z;
        cin >> z;
        v.push_back(z);
    }
    sort(v.begin(), v.end());

    int answer = 1; // 1 원을 만들 수 있는지부터 체크

    for(int i = 0; i < v.size(); i++){
        if(answer < v.at(i)){
            break;
        }
        answer += v.at(i);
    }

    cout << answer << endl;
    return 0;
}