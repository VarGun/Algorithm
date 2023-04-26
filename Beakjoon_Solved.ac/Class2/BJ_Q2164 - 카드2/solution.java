import java.util.*;

import java.io.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        double max = 0;
        for(int i = 0; i <= N; i++){
            if(N - Math.pow(2, i) <= 0){
                max = Math.pow(2, i);
                break;
            }
            
        }   
        System.out.println( (int)max - ((int)max - N)*2  );     
        

    }
    
}
