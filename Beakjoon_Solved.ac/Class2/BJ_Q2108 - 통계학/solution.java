import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        double am = 0;
        int[] bin = new int[8002]; // 최빈값 검사
        ArrayList<Integer> m = new ArrayList<Integer>(); // 중앙값과 범위 동시에 계산할 것.
        for(int i = 0; i<n;i++){
            int num = Integer.parseInt(br.readLine());
            am += num;
            m.add(num);
            bin[num + 4000] += 1;
        }
        Collections.sort(m);
        am /= n;
        int am1 = (int)am;
        if(am - am1 >= 0.5){ // 반올림
            am1 += 1;
        }
        else if(am - am1 <= -0.5){
            am1 -= 1;
        }
        int max = 0;
        ArrayList<Integer> num2 = new ArrayList<Integer>();
        for(int i = m.get(0); i <= m.get(m.size() -1); i++){ // 최솟값부터 최대값까지
            
            if(max <= bin[i+4000]){
                max = bin[i+4000];
            }
        }
        for(int i = m.get(0); i <= m.get(m.size() -1); i++){ // 최솟값부터 최대값까지
            if(max == bin[i+4000]){
               num2.add(i);
            }
        }
        
        bw.write(am1 + "\n");
        bw.write(m.get(m.size() / 2) + "\n");
        if(num2.size() >= 2){
            bw.write(num2.get(1) + "\n");
        }
        else{
            bw.write(num2.get(0) +"\n") ;
        }
        bw.write(m.get(m.size()-1) - m.get(0) + "\n");
        bw.flush();
        
    }
}
