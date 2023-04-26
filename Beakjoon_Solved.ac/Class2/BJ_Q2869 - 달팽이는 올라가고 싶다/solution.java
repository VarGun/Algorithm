import java.io.*;
import java.util.*;


public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        double a, b, v = 0;

        a = Long.parseLong(st.nextToken());
        b = Long.parseLong(st.nextToken());
        v = Long.parseLong(st.nextToken());

        bw.write(Integer.toString((int)(Math.ceil((v-a) / (a-b) ) + 1)));
        bw.flush();

    }
}