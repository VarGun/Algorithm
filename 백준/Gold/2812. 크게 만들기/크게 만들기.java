import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
  static int N, K, cur;
  static String[] tar;
  static Stack<Integer> stk;
  static Deque<Integer> dq;
  static int cnt;

  static void check(int cur){
    while (!dq.isEmpty()){
      if(dq.peekLast() < cur && cnt < K){
        dq.pollLast();
        cnt += 1;
      }else{
        dq.offerLast(cur);
        break;
      }
      if(cnt >= K){
        dq.offerLast(cur);
        break;
      }
      if(dq.isEmpty()){
        dq.offerLast(cur);
        break;
      }
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());
    tar = new StringTokenizer(br.readLine()).nextToken().split("");
    stk = new Stack<>();
    dq = new LinkedList<>();
    cnt = 0;

    for(int i = 0; i < N; i++){
      cur = Integer.parseInt(tar[i]);
      if(cnt >= K){
        dq.offerLast(cur);
        continue;
      }
      if(dq.isEmpty()){
        dq.offerLast(cur);
      }else{
        check(cur);
      }
    }

    for(int i = 0; i < K - cnt; i++){
      dq.pollLast();
    }

    while (!dq.isEmpty()){
      System.out.print(dq.getFirst());
      dq.pollFirst();
    }
  }
}