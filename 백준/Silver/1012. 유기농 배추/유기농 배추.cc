#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> dy = {0, 0, 1, -1};
vector<int> dx = {1, -1, 0, 0};
bool visited[50][50];
int field[50][50];
queue<pair<int, int>> q;
int N, M, K;
int ny, nx, cnt;

void bfs(int y, int x) {
  q.push({y, x});
  while (!q.empty()) {
    int yy = q.front().first;
    int xx = q.front().second;
    q.pop();

    for (int i = 0; i < 4; i++) {
      ny = yy + dy[i];
      nx = xx + dx[i];
      if (ny >= 0 && ny < N && nx >= 0 && nx < M && not visited[ny][nx] &&
          field[ny][nx] == 1) {
        visited[ny][nx] = true;
        q.push({ny, nx});
      }
    }
  }
}

void init() {
  cnt = 0;
  while (!q.empty()) q.pop();
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      field[i][j] = 0;
      visited[i][j] = false;
    }
  }
}

int main() {
  int T;
  cin >> T;
  while (T) {
    T--;
    int x, y;
    cin >> M >> N >> K;

    init();

    for (int i = 0; i < K; i++) {
      cin >> x >> y;
      field[y][x] = 1;
    }

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (field[i][j] == 1 && !visited[i][j]) {
          bfs(i, j);
          cnt += 1;
        }
      }
    }
    cout << cnt << '\n';
  }
}