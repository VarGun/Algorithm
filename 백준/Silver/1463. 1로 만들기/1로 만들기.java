import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.Queue;

public class Main {
  static int[] visited;
  static int N;

  static int bfs(int start){

    visited[start] = 0;
    Queue<Integer> q = new LinkedList<>();
    q.offer(start);
    while(!q.isEmpty()){
      int head = q.poll();
      if(head == 1){
        return visited[head];
      }
      ArrayList<Integer> tar = new ArrayList<>();
      if(head % 3 == 0){
        tar.add(head / 3);
      }
      if(head % 2 == 0){
        tar.add(head / 2);
      }
      if(head - 1 >= 0){
        tar.add(head - 1);
      }
      for(int t : tar){
        if(visited[t] == -1){
          visited[t] = visited[head] + 1;
          q.offer(t);
        }
      }
    }
    return 1;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());

    visited = new int[N + 1];
    Arrays.fill(visited, -1);
    System.out.println(bfs(N));;

  }
}