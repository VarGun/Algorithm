
import java.io.*;
import java.util.StringTokenizer;

public class solution {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int ans1;
        int ans2;
        if(m == 0){
            ans1 = (Integer.toString(n)).length();
            ans2 = (n>=100?n-100:100-n);
            System.out.println(ans1>ans2?ans2:ans1);
        }
        else{
            StringTokenizer st = new StringTokenizer(br.readLine());
            Integer[] nlist = new Integer[m];
            int tmp;
            int jud;
            for(int i = 0 ;i<m; i++){
                nlist[i] = Integer.parseInt(st.nextToken());
            }
            if(n == 100){
                System.out.println(0);
            }
            else if(n > 100){
                ans1 = n -100;
                ans2 = 2*n;
                tmp = ans2;
                for(int i = 0; i < ans2; i++){
                    String strI = Integer.toString(i);
                    jud = 0;
                    for(int j : nlist){
                        for(int k = 0; k < strI.length(); k++){
                            if(Character.getNumericValue(strI.charAt(k)) == j){
                                jud = 1;
                                break;
                            }
                        }
                        if(jud == 1){
                            break;
                        }
                    }
                    if(jud == 0){
                        if(i<=n){
                            tmp = n - i + strI.length();
                        }
                        else{
                            tmp = i - n + strI.length();
                        }
                    }
                    if(tmp < ans2){
                        ans2 = tmp;
                    }
                }
                System.out.println("ans1 : " + ans1+ " ans2 : " + ans2);
                System.out.println((ans1<ans2 ? ans1 : ans2));
            }
            else{ // n < 100
                ans1 = 100 - n;
                ans2 = 100 + n;
                tmp =  ans2;

                for(int i = 0; i < ans2; i++){
                    String strI = Integer.toString(i);
                    jud = 0;
                    for(int j :nlist){
                        for(int k = 0; k < strI.length(); k++){
                            if(Character.getNumericValue(strI.charAt(k)) == j){
                                jud = 1;
                                break;
                            }
                        }
                        if(jud == 1){
                            break;
                        }
                    }
                    if(jud == 0){
                        if(i<=n){
                            tmp = n - i + strI.length();
                        }
                        else{
                            tmp = i - n + strI.length();
                        }
                    }
                    if(tmp < ans2){
                        ans2 = tmp;
                    }

                }
                System.out.println("ans1 : " + ans1+ " ans2 : " + ans2);
                System.out.println((ans1<ans2 ? ans1 : ans2));

            }

            
        }

    }
}
