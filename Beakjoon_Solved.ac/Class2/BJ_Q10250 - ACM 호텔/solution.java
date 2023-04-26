import java.io.*;
import java.util.*;


public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for(int k = 0; k<T; k++){
            String s = br.readLine();
            StringTokenizer st = new StringTokenizer(s);
            int H = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int cnt = 0;
            for(int i = 1; i < W + 1; i++){
                for(int j = 1; j < H + 1; j++){
                    cnt++;
                    if(cnt == N){
                        bw.write(Integer.toString(j));
                        if(i < 10){
                            bw.write("0" + Integer.toString(i) + "\n");
                        }
                        else{
                            bw.write(Integer.toString(i) + "\n");
                        }  
                    }
                }
            }
        }
        bw.flush();


    }
}
