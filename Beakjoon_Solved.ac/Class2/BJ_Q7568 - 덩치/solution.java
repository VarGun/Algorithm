import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[][] nL = new int[n][2];


        for(int i = 0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            nL[i][0] = Integer.parseInt(st.nextToken());
            nL[i][1] = Integer.parseInt(st.nextToken());
            
        }

        for(int i = 0; i < n; i++){
            int cnt = 0;
            for(int j = 0; j < n; j++){
                if( i == j )
                continue;

                if(nL[i][0] < nL[j][0] && nL[i][1] < nL[j][1]){
                    cnt += 1;
                }   
            }
            bw.write(Integer.toString(1 + cnt) + " ");
        }
        
        
        bw.flush();


    }
}