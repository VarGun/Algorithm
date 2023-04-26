import java.io.*;
import java.util.*;


    public class solution {
        static int cnt;

        static void zz(int a, int b, int s){
            if(s == 1){
                return;
            }

            if(a < s/2 && b < s / 2 ){ // 1사분면
                zz(a, b, s/2);
            }
            else if(a < s / 2 && b >= s / 2 ){ // 2사분면
                cnt += s * s / 4;
                b -= s/2;
                zz(a, b, s/2);
            }
            else if(a >= s / 2 && b < s / 2 ){ // 3사분면
                cnt += s * s / 2;
                a -= s/2;
                zz(a, b, s/2);
            }
            else if(a >= s / 2 && b >= s / 2 ){ // 4사분면
                cnt += s * s / 4 * 3;
                a -= s/2;
                b -= s/2;
                zz(a, b, s/2);
            }
        }
        

        public static void main(String[] args) throws IOException{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());


            int s = (int) Math.pow(2, n);

            zz(r, c, s);

            System.out.println(cnt);

        }
    }
