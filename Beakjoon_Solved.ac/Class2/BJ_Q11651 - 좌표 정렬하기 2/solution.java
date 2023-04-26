import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int[][] cl = new int[N][2];
        int cnt = 0;
        while(cnt < N){
            StringTokenizer st = new StringTokenizer(br.readLine());
            cl[cnt][0] = Integer.parseInt(st.nextToken());
            cl[cnt][1] = Integer.parseInt(st.nextToken());

            cnt++;
        }
        Arrays.sort(cl, new Comparator<int[]>(){
            public int compare(int[] x1, int[] x2){
                return x1[1] - x2[1];
            }
        });
        Arrays.sort(cl, new Comparator<int[]>(){
            public int compare(int[] x1, int[] x2){
                if(x1[1] == x2[1]){
                    return x1[0] - x2[0];
                }
                else
                return x1[1] - x2[1];
            }
        });

        
        for(int i = 0; i < N; i++){
            bw.write(Integer.toString(cl[i][0]) + " " + Integer.toString(cl[i][1]) + "\n");
        }
        bw.flush();
    }
}