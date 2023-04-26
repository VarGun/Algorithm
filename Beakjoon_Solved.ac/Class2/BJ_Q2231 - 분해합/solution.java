import java.io.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for(int i = 0; i < N; i++){
            int k = i;
            int tem = i;
            while(tem != 0){
                k += tem % 10;
                tem /= 10;
            }
            if(k == N){
                System.out.println(i);
                break;
            }
            if(i == N ){
                System.out.println(0);
            }
            
        }
    }   
}
