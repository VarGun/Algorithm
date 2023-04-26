#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    vector<int> v;
    int cnt = 0;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    sort( v.begin(), v.end() );
    
    while(v.front() <= v.size()){
        if(v.front() == v.size()){
            if(v.at(v.size() - 1) > v.size()){
                break;
            }
        }
        int fr = v.front();
        vector<int>::iterator iter = v.begin();
        v.erase(iter + 1 - 1, iter + fr);
        cnt += 1;
    }
    cout << "result : " << cnt << endl;
    
}