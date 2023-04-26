import java.util.*;

public class solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int a = 1;
        int ans = 1;
        int cnt = 6;
        while(a < n){
            a+=cnt;
            cnt+=6;
            ans+=1;
        }
        System.out.println(ans);

    }
}
