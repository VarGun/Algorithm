import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
  static int N, M;
  static String[] p;
  static String[] tar;
  static boolean checkStr(int p_idx){
    for (int i = p_idx; i < p_idx + (2 * N + 1); i++) {
      if (!p[i].equals(tar[i - p_idx])) {
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    tar = new String[2 * N + 1];
    for (int i = 0; i < 2 * N + 1; i++) {
      if (i % 2 == 0) {
        tar[i] = "I";
      } else {
        tar[i] = "O";
      }
    }
    st = new StringTokenizer(br.readLine());
    M = Integer.parseInt(st.nextToken());
    st = new StringTokenizer(br.readLine());
    String pString = st.nextToken();

    p = pString.split("");

    int p_idx = 0;
    int len = tar.length;
    int answer = 0;
    boolean flag = false;
    while (p_idx <=  M - len) {
      if (p[p_idx].equals("I")) { // I 라면 검사
        flag = checkStr(p_idx);
      }
      if(flag){
        answer += 1;
        p_idx += 2;
        flag = false;
        continue;
      }
      p_idx += 1;
    }
    System.out.println(answer);
  }
}