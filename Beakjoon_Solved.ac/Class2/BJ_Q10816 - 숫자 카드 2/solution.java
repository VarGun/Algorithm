import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        int[] nl = new int[20000002];

        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);

        int val = 10000000;


        for(int i = 0; i< T;i++){
            nl[ Integer.parseInt(st.nextToken()) + val ] += 1;
        }

        int T2 = Integer.parseInt(br.readLine());

        String s2 = br.readLine();
        StringTokenizer st2 = new StringTokenizer(s2);

        for(int i = 0; i<T2; i++){
            int a = Integer.parseInt(st2.nextToken());
            bw.write(Integer.toString(nl[a+val]) + " ");
        }

        bw.flush();

    }
}