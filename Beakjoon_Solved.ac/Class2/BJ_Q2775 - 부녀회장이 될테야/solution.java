import java.io.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[][] apt = new int[15][15];
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < 15; i++){
            apt[0][i] = i + 1;
            apt[i][0] = 1;
        }
        for(int i = 1; i < 15; i++){
            for(int j = 1; j < 14; j++){
                apt[i][j] = apt[i-1][j] + apt[i][j-1];
            }
        }
        
        for(int i = 0; i<n; i++){
            int n1 = Integer.parseInt(br.readLine());
            int n2 = Integer.parseInt(br.readLine());
            bw.write(apt[n1][n2-1] + "\n");
        }
        bw.flush();



    }
}
