import java.util.*;

public class solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ans = 0;
        ans = sc.nextInt();
        sc.close();
        int num = 0; // 출력될 값
        int temp = 0; //임시 변수
        int n = 0; //순서
        int a = 0;  // 나머지용
        int cnt = 0; // 6의 갯수
        
        while(true){
            cnt = 0;
            num +=1;
            temp = num;
            while(true){
                a = num%10;
                num = num / 10;
                if(a == 6){
                    cnt += 1;
                    if(cnt >= 3){
                        n += 1;
                        break;
                    }
                }
                else{
                    cnt = 0;
                }
                if(num < 10){
                    if(num == 6){
                        cnt +=1;
                        if(cnt >= 3){
                            n += 1;
                            break;
                        }
                    }
                    break;
                }
            }
            if(n == ans){
                System.out.println(temp);
                break;
            }
            num = temp;
            
        }
    }
}
