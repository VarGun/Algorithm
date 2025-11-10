
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
  static int n, m, zCnt;
  static int[][] board;
  static ArrayList<int[]> tv;
  static int[][] dirs = {

      {-1, 0}, {0, 1}, {1, 0}, {0, -1}, // 상우하좌 (시계)
  };
  static int[][][] num_dirs = {
      {{0}, {1}, {2}, {3}},
      {{0, 2}, {1, 3}},
      {{0, 1}, {1, 2}, {2, 3}, {3, 0}},
      {{0, 1, 2}, {1, 2, 3}, {2, 3, 0}, {3, 0, 1}},
      {{0, 1, 2, 3}}
  };

  public static boolean checkBoundary(int y, int x) { // 경계 벗어나는지 체크
    return x >= 0 && y >= 0 && x < m && y < n;
  }

  public static void checkTv(int[][] board, int y, int x, int dir) {
    int tmpX = x;
    int tmpY = y;
    while (checkBoundary(tmpY, tmpX)) {
      tmpY += dirs[dir][0];
      tmpX += dirs[dir][1];
      if(!checkBoundary(tmpY, tmpX ) || board[tmpY][tmpX] == 6) {
        break;
      }
      if(board[tmpY][tmpX] == 0) {
        board[tmpY][tmpX] = -1;
      }
    }

  }

  public static void backT(int[][] board, int depth){
    if(depth == tv.size()){
      zCnt = Math.min(zCnt, calcZero(board));
      return;
    }
    int[] cctv = tv.get(depth);
    int y = cctv[0];
    int x = cctv[1];
    int type = cctv[2];

    for (int i = 0; i < num_dirs[type - 1].length; i++){
      int[][] tmpBoard = new int[n][m];
      for(int a = 0; a < n; a++){ tmpBoard[a] = board[a].clone();};
      for (int j = 0; j < num_dirs[type - 1][i].length; j++) {
        checkTv(tmpBoard, y, x, num_dirs[type - 1][i][j]);
      }
      backT(tmpBoard, depth + 1);


    }

  }

  public static int calcZero(int[][] board){
    int z_cnt = 0;
    for(int i = 0; i < board.length; i++){
      for(int j = 0; j < board[i].length; j++){
        if(board[i][j] == 0){
          z_cnt += 1;
        }
      }
    }
    return z_cnt;
  }


  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    zCnt = n * m;
    board = new int[n][m];
    tv = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < m; j++) {
        int cur = Integer.parseInt(st.nextToken());
        board[i][j] = cur;
        if(cur != 0 && cur != 6){
          tv.add(new int[]{i, j, cur});
        }
      }
    }
    backT(board, 0);
    System.out.println(zCnt);
  }
}
