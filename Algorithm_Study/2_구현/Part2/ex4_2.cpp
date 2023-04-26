#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main(){
    string str;
    cin >> str;
    int x = str.at(0) - '0' - 48;
    int y = str.at(1) - '0';
    cout << x << " " <<  y << endl;

    int dx[8] = {2, 2, -2, -2, 1, -1, -1, 1};
    int dy[8] = {1, -1, 1, -1, 2, 2, -2, -2};
    int answer = 0;
    for(int i = 0; i < 8; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx > 8 || nx < 1 || ny > 8 || ny < 1){ 
            continue;
        }
        cout <<"dx[i] : "<< dx[i] << ", dy[i] : " << dy[i] <<endl;
        answer += 1;
    }
    
    cout << answer << endl;
}