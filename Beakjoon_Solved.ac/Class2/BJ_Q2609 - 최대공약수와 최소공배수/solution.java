import java.util.*;

public class solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int n1 = n;
        int m1 = m;
        int gcd = 0;
        if(n < m){
            n1 = m;
            m1 = n;
        }
        while(m1 != 0){
            gcd = m1;
            m1 = n1 % m1;
            n1 = gcd;
        }

        int lcm = 0;


        lcm = (n * m) / gcd;

        System.out.println(gcd);
        System.out.println(lcm);

    }
}
