#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    string x;
    cin >> x;
    int result = 0;
    for(int i = 0; i<x.size(); i++){
        if(x.at(i) != '0'){ // 0 이 아닌 경우만 보도록
            if(result == 0){
                result += x.at(i) - '0';
            }
            else if(result == 1){
                if(x.at(i) == '1'){
                    result += 1;
                }
                else{
                    result *= x.at(i) - '0';
                }
            }
            else{
                if(x.at(i) == '1'){
                    result += 1;
                }
                else{
                    result *= x.at(i) -'0';
                }
            }
        }
    }
    cout << result << endl;

}