import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
        int[] nL = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < n ; i++){
            nL[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nL);

        long ans;
        int ans2 = 0;
        int high = nL[n-1];
        int low = 0;
        int mid = 0;
        while(low <= high){
            mid = (high + low) / 2;
            ans = 0;
            for(int i = 0; i < n; i++){
                if(nL[i] > mid){
                    ans += nL[i] - mid;
                }

            }
            if(ans < m){
                high = mid - 1;
            }
            else{
                low = mid + 1;
                ans2 = mid;
            }
        }
        System.out.println(ans2);
    }   
}