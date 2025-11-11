import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
  static int N, M;
  static HashSet<String> hs;
  static HashSet<String> hs2;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    hs = new HashSet<>();
    hs2 = new HashSet<>();
    String cur;

    for(int i = 0; i < N; i++) {

      String line = br.readLine();
      if (line == null || line.trim().isEmpty()) continue; // 안전하게 처리

      st = new StringTokenizer(line);
      hs.add(st.nextToken());
    }
    for(int i = 0; i < N; i++) {
      String line = br.readLine();
      if (line == null || line.trim().isEmpty()) continue; // 안전하게 처리

      st = new StringTokenizer(line);
      cur = st.nextToken();
      if(hs.contains(cur)) {
        hs2.add(cur);
      }
    }
    List<String> tmpList = new ArrayList<>(hs2);
    Collections.sort(tmpList);
    System.out.println(tmpList.size());
    for(String s:tmpList) {
      System.out.println(s);
    }

  }
}