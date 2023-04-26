#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<string> split(string str, char d){
    istringstream iss(str);
    string buffer;
    vector<string> result;
    while(getline(iss, buffer, d)){
        result.push_back(buffer);
    }
    return result;
}
int main(){
    int n;
    cin >> n;
    cin.ignore(); // 입력 버퍼 비우기
    string dir;
    getline(cin, dir);
    vector<string> v = split(dir, ' ');
    int x = 1; 
    int y = 1;

    for(int i = 0; i < v.size(); i++){
        if(y != 1 && (v.at(i)).compare("L") == 0){
            y -= 1;
            cout << v.at(i) << " : " << x <<" " << y << endl;
        }
        else if( y != n && (v.at(i)).compare("R") == 0){
            y += 1;
            cout << v.at(i) << " : " << x <<" " << y << endl;
        }
        else if(x != 1 && (v.at(i)).compare("U") == 0){
            x -= 1;
            cout << v.at(i) << " : " << x <<" " << y << endl;
        }
        else if(x != n && (v.at(i)).compare("D") == 0){
            x += 1;
            cout << v.at(i) << " : " << x <<" " << y << endl;
        }
    }
    cout << x << " " << y << endl;
}