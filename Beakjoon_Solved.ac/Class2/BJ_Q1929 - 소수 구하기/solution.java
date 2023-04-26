import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        
        Scanner sc = new Scanner(System.in);
        int n, m = 0;
        n = sc.nextInt();
        m = sc.nextInt();
        sc.close();
        boolean[] ans = new boolean[m+1];
        ans[1] = true;

        for(int i= 2; i < ans.length; i++) {
            for(int j = 2; i*j < ans.length; j++) {
                ans[i*j] = true;
            }
        }


        for(int i = n; i<= m; i++){
            if(ans[i] != true){ 
                System.out.println(i);
            }
        }

    }
    
    
}
