import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        int n = 0;
        long m = 0;
        n = sc.nextInt();
        m = sc.nextInt();
        long[] nlist = new long[n];
        for(int i = 0; i < n; i++){
            nlist[i] = sc.nextInt();
        }
        sc.close();
        Arrays.sort(nlist);
        

        long high = nlist[n-1];
        long low = 1;
        long mid = 0;
        
        while(low <= high){
            mid = (high + low) / 2;
            long cnt = 0;
            for(int i = 0; i < n; i++){
                cnt += nlist[i] / mid;
            }
            if(cnt >= m){
                low = mid + 1;  
            }
            else if( cnt < m){
                high = mid - 1;   
            }
        }
        System.out.println(high);
    }
}