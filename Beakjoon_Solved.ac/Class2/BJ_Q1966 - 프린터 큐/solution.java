import java.io.*;

import java.util.StringTokenizer;

public class solution {
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int c = Integer.parseInt(br.readLine());
        for(int g = 0; g < c; g++){
            String s = br.readLine();
            StringTokenizer st = new StringTokenizer(s);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int[] num = new int[10000]; // 주어지는 중요도
            int ans = 0; // 순서
            int[] on = new int[9];
            String s2 = br.readLine();
            StringTokenizer st2 = new StringTokenizer(s2);
            if(a == 1 ){
                ans += 1;
                bw.write(ans + "\n");
            }
            else{
                for(int i = 0; i < a; i++){
                    int t = Integer.parseInt(st2.nextToken());
                    num[i] = t;
                    on[t-1] += 1;
                }
                for(int i = 0; i < num.length; i++){
                    if(i == b){ //m일때
                        if(num[i] == 9){
                            ans +=1;
                            bw.write(ans + "\n");
                            break;
                        }
                        else{
                            int cnt = 0;
                            for(int j = num[i]; j < 9; j++){
                                if(on[j] != 0){
                                    cnt += 1;
                                }
                            }
                            if(cnt != 0){ 
                                num[i+a-ans] = num[i];
                                b = b+a-ans;                         
                            }
                            else if(cnt == 0){
                                ans += 1;
                                bw.write(ans + "\n");
                                break;
                            }
                        }
                    }
                    else{
                        if(num[i] == 9){
                            ans +=1;
                            on[num[i]-1] -=1;
                        }
                        else{
                            int cnt = 0;
                            for(int j = num[i]; j < 9; j++){
                                if(on[j] != 0){
                                    cnt += 1;
                                }
                            }
                            if(cnt != 0){
                                num[i+a-ans] = num[i];
                            }
                            else if(cnt == 0){
                                ans += 1;
                                on[num[i]-1] -=1;
                            }
                        }
                    }


                }

            }

        }
        bw.flush();
    }
    
}
