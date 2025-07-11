import java.io.*;

public class Main{
    static int m;
    static int n;
    static int k;
    static int[][] bg;
    static boolean[][] visit;
    static int bug;
    static int[][] dr = {{-1,0}, {1,0}, {0, -1}, {0, 1}};

    
    static void dfs(int a, int b){
        visit[a][b] = true;
        for(int i = 0; i < 4; i++){
            int c = a + dr[i][0];
            int d = b + dr[i][1];

            if (c >= 0 && d >= 0 && c < m && d < n) {
				if(bg[c][d] == 1 && visit[c][d] == false){ // 1이고 방문 x
                    dfs(c,d);
                }
			}
        }   
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        for(int i = 0; i<t; i++){
            String[] s = br.readLine().split(" ");
            m = Integer.parseInt(s[0]);
            n = Integer.parseInt(s[1]);
            k = Integer.parseInt(s[2]);
            bg = new int[m][n];
            visit = new boolean[m][n];
            bug = 0;


            for(int j = 0; j < k; j++){
                String[] s2 = br.readLine().split(" ");
                bg[Integer.parseInt(s2[0])][Integer.parseInt(s2[1])] = 1;  
            }

            for(int j = 0; j < m; j++){
                for(int l = 0; l < n; l++){
                    if(bg[j][l] == 1 && visit[j][l] == false){
                        dfs(j, l);
                        bug++;
                    }

                }
            }
            bw.write(Integer.toString(bug)+"\n");
        }

        bw.flush();
    }
    





}