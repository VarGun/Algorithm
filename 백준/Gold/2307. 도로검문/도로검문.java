import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  static int n, m, res, ans;
  static int INF = 500000000;

  static List<List<Node>> graph;

  static boolean[] visited;

  public static int[] dijkstra(int start, int n1, int n2) {
    int[] dist = new int[n + 1];
    Arrays.fill(dist, INF);
    dist[start] = 0;

    PriorityQueue<Node> pq = new PriorityQueue<>();
    pq.offer(new Node(start, 0));

    while (!pq.isEmpty()) {
      Node cur = pq.poll();
      int now = cur.v;
      int cost = cur.c;
      if (cost > dist[now])
        continue;
      for (Node nxt : graph.get(cur.v)) {
        if ((nxt.v == n1 && now == n2) || (nxt.v == n2 && now == n1)) {
          continue;
        }
        if (dist[nxt.v] > cost + nxt.c) {
          dist[nxt.v] = cost + nxt.c;
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

    int[][] paths = new int[m][3];
    graph = new ArrayList<>();
    visited = new boolean[n + 1];

    for (int i = 0; i <= n; i++) {
      graph.add(new ArrayList<>());
    }

    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int n1 = Integer.parseInt(st.nextToken());
      int n2 = Integer.parseInt(st.nextToken());
      int d = Integer.parseInt(st.nextToken());
      paths[i][0] = n1;
      paths[i][1] = n2;
      paths[i][2] = d;

      graph.get(n1).add(new Node(n2, d));
      graph.get(n2).add(new Node(n1, d));
    }

    int[] dist1 = dijkstra(1, -1, -1); // 1 -> i 까지 최단거리
    int[] dist2 = dijkstra(n, -1, -1); // n -> i 까지 최단거리
    int base = dist1[n];

    int _max = -1;
    for (int[] p : paths) {
      int n1 = p[0];
      int n2 = p[1];
      int d = p[2];

      if ((dist1[n1] != INF && dist2[n2] != INF && dist1[n1] + d + dist2[n2] == base)
          || (dist1[n2] != INF && dist2[n1] != INF && dist1[n2] + d + dist2[n1] == base)) {
        int[] tmpDist = dijkstra(1, n1, n2);
        if (tmpDist[n] >= INF) {
          System.out.println(-1);
          return;
        }
        _max = Math.max(_max, tmpDist[n] - dist1[n]);
      }
    }
    System.out.println(_max);
  }
}


class Node implements Comparable<Node> {
  int v;
  int c;

  Node(int v, int c) {
    this.v = v;
    this.c = c;
  }

  @Override
  public int compareTo(Node o) {
    return this.c - o.c;
  }
}
