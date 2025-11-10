import java.io.*;
import java.util.*;

public class Main {

  static class Node implements Comparable<Node> { // ✅ 변경 ①
    int v, c;
    Node(int v, int c) { this.v = v; this.c = c; }
    public int compareTo(Node o) { return this.c - o.c; } // ← Comparator 제거하고 내부에서 정렬
  }

  static int n, m;
  static int INF = 500000000; // ✅ 변경 ② : 기존 5,000,000 → 500,000,000 (안전한 INF 값)
  static List<List<Node>> graph; // ✅ 변경 ③ : ArrayList<Node>[] → List<List<Node>> 로 일관성 있게 변경

  static int[] dijkstra(int start, int ignoreU, int ignoreV) {
    int[] dist = new int[n + 1];
    Arrays.fill(dist, INF);
    dist[start] = 0;

    PriorityQueue<Node> pq = new PriorityQueue<>();
    pq.offer(new Node(start, 0));

    while (!pq.isEmpty()) {
      Node cur = pq.poll();
      if (cur.c > dist[cur.v]) continue;

      for (Node nxt : graph.get(cur.v)) {
        // ✅ 변경 ④ : 간선 차단 조건 동일하지만, cur.v 기준으로 처리 (명확한 방향성)
        if ((cur.v == ignoreU && nxt.v == ignoreV) || (cur.v == ignoreV && nxt.v == ignoreU))
          continue;

        if (dist[nxt.v] > dist[cur.v] + nxt.c) {
          dist[nxt.v] = dist[cur.v] + nxt.c;
          pq.offer(new Node(nxt.v, dist[nxt.v]));
        }
      }
    }
    return dist;
  }

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    graph = new ArrayList<>();
    for (int i = 0; i <= n; i++) graph.add(new ArrayList<>()); // ✅ 변경 ⑤ : 리스트 초기화 구조 개선

    int[][] edges = new int[m][3]; // ✅ 변경 ⑥ : 경로를 int[][] 로 단순화

    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int u = Integer.parseInt(st.nextToken());
      int v = Integer.parseInt(st.nextToken());
      int w = Integer.parseInt(st.nextToken());
      edges[i][0] = u;
      edges[i][1] = v;
      edges[i][2] = w;

      graph.get(u).add(new Node(v, w));
      graph.get(v).add(new Node(u, w));
    }

    int[] dist1 = dijkstra(1, -1, -1);
    int[] dist2 = dijkstra(n, -1, -1);
    int base = dist1[n];
    int maxDelay = -1;

    for (int[] e : edges) {
      int u = e[0], v = e[1], w = e[2];

      // ✅ 변경 ⑦ : 최단경로 포함 조건에서 dist1/dist2 존재 검증 추가 (INF 방지)
      if ((dist1[u] != INF && dist2[v] != INF && dist1[u] + w + dist2[v] == base)
          || (dist1[v] != INF && dist2[u] != INF && dist1[v] + w + dist2[u] == base)) {

        int[] newDist = dijkstra(1, u, v);
        if (newDist[n] >= INF) {
          System.out.println(-1);
          return;
        }
        maxDelay = Math.max(maxDelay, newDist[n] - base);
      }
    }

    System.out.println(maxDelay);
  }
}
