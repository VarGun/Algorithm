import java.io.*;
import java.util.StringTokenizer;


public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        int ans = 0;
        for(int g = 0; g < N; g++){
            int a = Integer.parseInt(st.nextToken());
            int cnt = 0;
            if(a == 2){
                ans += 1;
            }
            else if(a > 2){
                for(int i = 2; i < a; i++ ){
                    if( a%i == 0){
                        cnt = 1;
                        break;
                    }
                }
                if(cnt == 0){ 
                    ans += 1;
                }
            }
            
        }
        System.out.println(ans);
    }
}
