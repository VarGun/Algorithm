#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<string> split(string str, char delimiter);

int main(){
    vector<int> v;
	int n, m, k;
	cin >> n >> m >> k;

	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		v.push_back(x);
	}

	sort(v.begin(), v.end());
    
	int f_num= v[n - 1];
	int s_num = v[n - 2];
    cout << ((k * f_num) + s_num) * (m / (k + 1)) + (m % (k+1)) * f_num;

    return 0;
}