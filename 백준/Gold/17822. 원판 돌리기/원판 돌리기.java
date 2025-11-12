import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main {
  static int N, M, T;
  static int[][] cir;
  static int[][] com;
  static HashSet<String> dupSet;
  static int total;
  static int total_cnt;

  static void rotate(int x, int d, int k){
    int[] tmp = new int[M];

    for(int i = 0; i < N; i ++){

      if((i + 1) % x == 0){ // 대상 원판
        if(d == 0){ // 시계 방향
          for(int j = 0; j < M; j++){
            if(j - k < 0){
              tmp[j] = cir[i][M - k + j];
            }else{
              tmp[j] = cir[i][j - k];
            }
          }
        }
        else{
          for(int j = 0; j < M; j++){
            tmp[j] = cir[i][(j + k) % M];
          }
        }
        cir[i] = tmp.clone();
      }
    }
  }

  static boolean checkDup(){
    dupSet = new HashSet<>();

    total = 0;
    total_cnt = 0;
    for(int i = 0; i < N - 1; i++){
      for(int j = 0; j < M; j++){
        int tar = cir[i][j];
        if(tar == -1){
          continue;
        }
        total += cir[i][j];
        total_cnt += 1;
        // 바깥 쪽
        if(tar == cir[i + 1][j] && cir[i + 1][j] != -1){
          dupSet.add(i + "," + j);
          dupSet.add(i + 1 + "," + j);
        }
        // 오른 쪽
        if(tar == cir[i][(j + 1) % M] &&  cir[i][(j + 1) % M] != -1){
          dupSet.add(i + "," + j);
          dupSet.add(i + "," + (j + 1) % M);
        }
      }
    }
    // 맨 바깥 쪽
    for(int i = 0; i < M; i ++){
      if(cir[N - 1][i] != -1){
        total += cir[N - 1][i];
        total_cnt += 1;
        if(cir[N -1][i] == cir[N - 1][(i + 1) % M]
            && cir[N - 1][(i + 1) % M] != -1 ){
          dupSet.add(N - 1 + "," + i);
          dupSet.add(N - 1 + "," + (i + 1) % M);

        }
      }
    }

    if(dupSet.isEmpty()){
      return false; // 중복 없음.
    }
    return true; // 중복 있음.
  }

  static void delDup(){
    for(String it : dupSet){
      String[] item = it.split(",");
      cir[Integer.parseInt(item[0])][Integer.parseInt(item[1])] = -1;
    }
  }

  static void setAvg(){
    double avg = (double) total / total_cnt;
    for(int  i = 0; i < N; i++){
      for(int j= 0; j < M; j++){
        int tar = cir[i][j];
        if(tar == -1){
          continue;
        }
        if(tar > avg){
          cir[i][j] -= 1;

        }else if(tar < avg){
          cir[i][j] += 1;

        }
      }
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    T = Integer.parseInt(st.nextToken());
    cir = new int[N][M];
    com = new int[T][3];
    for(int i = 0; i < N; i++){
      st = new StringTokenizer(br.readLine());
      for(int j = 0; j < M; j++){
        cir[i][j] = Integer.parseInt(st.nextToken());
      }
    }
    for(int i = 0; i < T; i++){
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int d = Integer.parseInt(st.nextToken());
      int k = Integer.parseInt(st.nextToken()) % M;
      rotate(x, d, k);
      if(checkDup()) {
        delDup();
      }
      else{
        setAvg();
      }
    }

    int answer = 0;
    for(int[] curLine : cir){
      for(int item : curLine){
        if(item != -1){
          answer += item;
        }
      }
    }
    System.out.println(answer);
  }
}