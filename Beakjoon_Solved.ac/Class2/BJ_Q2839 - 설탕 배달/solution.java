import java.util.*;

public class solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int n2 = n;
        int mo = 0;
        int[] al = new int[2];
        if(n%5==0){
            System.out.println(n/5);
        }
        
        else{
            if(n%3 == 0){
                al[0] = n/3;
            }
            for(int i = 0; i < n; i++){
                n -= 3;
                al[1] += 1;

                if(n % 5 == 0){
                    al[1] += n/5;
                    break;
                }
                if( i*3 > n2 || n < 5){
                    mo = 1;
                    break;
                }
            }
            if(mo == 1 && al[0] == 0){ // 3의 배수도 안되고 다른 경우도 안될때
                System.out.println(-1);
            }
            else if(mo == 1 && al[0] != 0){ // 3의 배수일때
                System.out.println(al[0]);
            }
            else if(mo != 1 && al[0] == 0){ // 그 경우일때
                System.out.println(al[1]);
            }
            else if(mo != 1 && al[0] != 0){ // 둘 다 일때
                if(al[0] > al[1]){
                    System.out.println(al[1]);
                }
                else{
                    System.out.println(al[0]);
                }
            }


        }

    }
}