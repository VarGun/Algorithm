import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        String[][] sl = new String[T][2];

        int cnt = 0;

        while(cnt < T){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            String s2 = st.nextToken();
            sl[cnt][0] = s;
            sl[cnt][1] = s2;
            cnt++;
        }

        Arrays.sort(sl, new Comparator<String[]>(){
            public int compare(String[] n1, String[] n2){
                return Integer.compare( Integer.parseInt(n1[0]), Integer.parseInt(n2[0]) );
            }
        });
        

        for(int i = 0; i < T; i++){
            bw.write(sl[i][0] + " " + sl[i][1] + "\n" );
        }
        bw.flush();

        
        
    }
}
