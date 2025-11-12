import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
  static int v, n, n1, n2, maxI, maxDis;
  static List<List<Node>> tr;
  static int[] dis;
  static int INF;

  static void getMaxDis() {
    for (int i = 1; i <= v; i++) {
      if (dis[i] != INF && dis[i] > maxDis) {
        maxI = i;
        maxDis = dis[i];
      }
    }
  }

  static void dijkstra(int start) {
    PriorityQueue<Node> pq = new PriorityQueue<>();
    pq.add(new Node(start, 0));
    dis = new int[v + 1];

    Arrays.fill(dis, INF);

    dis[start] = 0;
    while (!pq.isEmpty()) {
      Node head = pq.poll();
      int now = head.v;
      int cost = head.c;
      if (cost > dis[now]) {
        continue;
      }
      for (Node nxt : tr.get(now)) {
        int newDis = dis[now] + nxt.c;
        if (newDis < dis[nxt.v]) {
          pq.add(new Node(nxt.v, newDis));
          dis[nxt.v] = newDis;
        }
      }
    }

  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    v = Integer.parseInt(st.nextToken());
    tr = new ArrayList<>();
    INF = 100_000_0000;

    for (int i = 0; i <= v; i++) {

      tr.add(new ArrayList<>());
    }

    for (int i = 0; i < v; i++) {

      st = new StringTokenizer(br.readLine());

      n = Integer.parseInt(st.nextToken());

      n1 = Integer.parseInt(st.nextToken());

      while (n1 != -1) {
        n2 = Integer.parseInt(st.nextToken());
        tr.get(n).add(new Node(n1, n2));
        n1 = Integer.parseInt(st.nextToken());
      }
    }

    maxDis = -1;
    dijkstra(1);

    getMaxDis();
    dijkstra(maxI);
    getMaxDis();
    System.out.println(maxDis);
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

  @Override
  public String toString() {
    String tmp = "v : " + this.v + ", c : " + this.c;
    return tmp;
  }
}