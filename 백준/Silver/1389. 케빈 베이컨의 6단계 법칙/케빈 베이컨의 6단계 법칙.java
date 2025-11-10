import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.Queue;

public class Main {
  static int n, m;
  static ArrayList<ArrayList<Integer>> graph;
  static int[] dist;

  public static int bfs(int start){

    int cnt = 0;
    int[] visited = new int[n + 1];
    Arrays.fill(visited, -1);
    visited[start] = 0;
    Queue<Integer> q = new LinkedList<>();
    q.offer(start);
    while(!q.isEmpty()){
      int head = q.poll();
      for(int i = 0; i < graph.get(head).size(); i++){
        if(visited[graph.get(head).get(i)] == -1){
          int nxt = graph.get(head).get(i);
          visited[nxt] = visited[head] + 1;
          q.offer(nxt);
          cnt += visited[nxt];
        }
      }
    }
    return cnt;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    graph = new ArrayList<>();

    dist = new int[n + 1];

    for(int i = 0; i <= n; i++){
      graph.add(new ArrayList<>());
    }
    for(int i = 0; i < m; i++){
      st = new StringTokenizer(br.readLine());
      int n1 = Integer.parseInt(st.nextToken());
      int n2 = Integer.parseInt(st.nextToken());
      graph.get(n1).add(n2);
      graph.get(n2).add(n1);
    }
    int _min = n * m;
    ArrayList<Integer> ans = new ArrayList<>();

    for(int i = 1; i <= n; i++){
      int cur = bfs(i) + 1; // 0 번째 자리 -1 고려
      if(_min > cur){
        ans = new ArrayList<>();
        ans.add(i);
        _min = cur;
      } else if (_min == cur) {
        ans.add(i);
      }
    }
    System.out.println(ans.get(0));
    br.close();
  }
}