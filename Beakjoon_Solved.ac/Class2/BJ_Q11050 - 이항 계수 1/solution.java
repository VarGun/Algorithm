import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int nf = 1;
        int kf = 1;
        for(int i = N; i > N - K; i--){
            nf *= i;
        }
        for(int i = K; i > 0; i--){
            kf *= i;
        }
        
        System.out.println(nf / kf);

    }
}