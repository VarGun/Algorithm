#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int cnt = 0;
    int n, k;
    cin >> n >> k;
    while( n != 1){
        if( n % k == 0){
            n /= k;
        }
        else{
            n-=1;
        }
        cnt += 1;        
    }
    cout << cnt << endl;

}