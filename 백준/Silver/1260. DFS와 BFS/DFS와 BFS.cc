#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void dfs(int node, vector<bool>& visited, vector<vector<int>>& graph) {
  visited[node] = true;
  cout << node << ' ';
  for (int i = 0; i < graph[node].size(); i++) {
    if (!visited[graph[node][i]]) {
      dfs(graph[node][i], visited, graph);
    }
  }
}
void bfs(int node, vector<vector<int>> graph) {
  queue<int> q;
  int cur;
  q.push(node);
  vector<bool> visited(graph.size() + 1, false);
  visited[node] = true;

  while (!q.empty()) {
    cur = q.front();
    cout << cur << ' ';
    q.pop();
    for (int i = 0; i < graph[cur].size(); i++) {
      if (!visited[graph[cur][i]]) {
        q.push(graph[cur][i]);
        visited[graph[cur][i]] = true;
      }
    }
  }
}

int main() {
  int N, M, V, n1, n2;

  cin >> N >> M >> V;

  vector<vector<int>> graph(N + 1, vector<int>());
  vector<bool> visited(N + 1, false);

  for (int i = 0; i < M; i++) {
    cin >> n1 >> n2;
    graph[n1].push_back(n2);
    graph[n2].push_back(n1);
  };

  for (int i = 1; i < N + 1; i++) {
    sort(graph[i].begin(), graph[i].end());
  }

  dfs(V, visited, graph);
  cout << '\n';
  bfs(V, graph);
}