#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    vector<int> v;
    int n,m;
    cin >> n >> m;

    for(int i = 0; i < n; i++){
        int z;
        cin >> z;
        v.push_back(z);
    }
    int cnt = 0;
    for(int i = 0; i < v.size() - 1; i++){
        for(int j = i + 1; j <v.size(); j++){
            if(v.at(i) != v.at(j)){
                cout << "i : " << v.at(i) <<    ", j : " << v.at(j) << endl;
                cnt += 1;
            }
        }
    }
    cout << cnt << endl;
    return 0;
}