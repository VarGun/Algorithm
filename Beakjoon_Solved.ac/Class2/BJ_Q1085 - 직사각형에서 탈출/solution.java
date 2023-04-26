import java.util.Scanner;

public class solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = 0;
        int[] alist = new int[4];
        int[] alist2 = new int[4];

        for(int i = 0; i < 4 ; i++){
            a = sc.nextInt();
            alist[i] = a;
        }
        alist2[0] = alist[0];
        alist2[1] = alist[1];
        alist2[2] = alist[2] - alist[0];
        alist2[3] = alist[3] - alist[1];

        int ans = alist2[0];
        for(int i = 0; i < 4; i++){
            if(alist2[i] < ans){
                ans = alist2[i];
            }
        }
        sc.close();
        System.out.println(ans);

    }
}
