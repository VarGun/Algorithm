import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int[] nl2 = new int[N];
        for(int i = 0; i < N; i++){
            nl2[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(nl2);
        
        for(int i = 0; i < N; i++){
            bw.write(Integer.toString(nl2[i]) + "\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
