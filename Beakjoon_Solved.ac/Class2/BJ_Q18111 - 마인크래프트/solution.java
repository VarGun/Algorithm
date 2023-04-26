import java.util.*;

import java.io.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        
        ArrayList<Integer> gr2 = new ArrayList<Integer>(); // 값 받는 list


        int max = 0;
        int min = 2147483647;
        for(int i = 0; i < n; i++){
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                int c = Integer.parseInt(st2.nextToken());
                gr2.add(c);
                max = Math.max(max, c);
                min = Math.min(min, c);
            }
        }
        int aT = 2147483647;
        int aH = 0;
        for(int i = min; i<=max; i++){
            int b2 = b;
            int t1 = 0;
            // i가 목표 높이
            for(int j = 0; j < n*m; j++){
                int t = gr2.get(j);
                if(t > i){ // 목표까지 지우기
                    t1 += 2 * ( t - i );
                    b2 += t - i;
                }
                else if(t < i){ // 목표까지 채우기
                    t1 += (i -t);
                    b2 -= i - t;
                    
                }
                else
                continue;

            }
            if(b2 < 0){
                continue;
            }
            
            if(aT >= t1){
                aT = t1;
                aH = i;
            }
            

        }
        
        bw.write(Integer.toString(aT) + " " + Integer.toString(aH));

        bw.flush();
        


    }

}
