#include <iostream>
#include <vector>

using namespace std;
int cntZ = 0, cntO = 0;

int fibo(int n){
  if (n == 0){
    cntZ += 1;
    return 0;
  } else if(n == 1){
    cntO += 1;
    return 1;
  } else{
    return fibo(n - 1) + fibo(n - 2);
  };
}

int main(){
  int T, N;
  cin >> T;
  vector<int> v(43);
  v[0] = 0, v[1] = 1;

  for(int i = 2; i < v.size(); i++){
    v[i] = v[i - 1] + v[i - 2];
  }
  
  while(T){
    T--;
    cin >> N;
    if(N == 0){
      cout << 1 << ' ' << 0 << '\n';
    }
    else cout << v[N - 1] << ' ' <<  v[N] << '\n';
  }
}