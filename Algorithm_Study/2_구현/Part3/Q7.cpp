#include <iostream>
#include <vector>

using namespace std;

int main(){
    string x;
    cin >> x;
    int n1 = 0;
    int n2 = 0;
    string answer = "READY";
    for(int i = 0; i < x.size() / 2; i++){
        n1 += x.at(i) -'0';
    }
    for(int i = x.size() / 2; i < x.size(); i++){
        n2 += x.at(i) -'0';
    }
    if(n1 == n2){
        answer = "LUCKY";
    }
    cout << answer << endl;
}