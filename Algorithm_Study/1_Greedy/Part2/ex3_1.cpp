#include <iostream>
using namespace std;

int main(){
    int money;
    cout << "���� �ݾ� : ";
    cin >> money;

    int answer = 0;
    int coin[4] = { 500, 100, 50, 10};

    for(int i = 0; i < 4; i++){
        answer += money / coin[i];
        money %= coin[i];
    }
    cout <<"answer : " << answer <<endl;

    return 0;
}