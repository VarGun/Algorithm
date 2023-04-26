#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> v;
    int n, m;

    cin >> n >> m;
    int min_array[n];
    int array[n][m];

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            int x;
            cin >> x;
            array[i][j] = x;
        }
    }

    for(int i = 0; i < n; i++){
        int min_num = 10001;
        for(int j = 0; j < m; j++){
            if(array[i][j] < min_num ){
                min_num = array[i][j];
            }
        }
        v.push_back(min_num);
    }

    sort(v.begin(), v.end());

    cout << v[n-1];

}