import java.util.*;
import java.io.*;

public class solution {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        long a = 0;
        long pow = 1;
        int r = 31;
        int m = 1234567891;
        
        for(int i = 0; i < n; i++){
            a +=  ( s.charAt(i) -'a' + 1) * pow;
            pow *= r;
            pow %= m;
            
        }
        System.out.println(a% m);
    }
}