import java.io.*;
import java.util.ArrayList;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        ArrayList<Integer> al = new ArrayList<Integer>();
        int cnt = 0;
        while(cnt < T){
            int n = Integer.parseInt(br.readLine());
            if(n != 0){
                al.add(n);
            }
            else{
                al.remove(al.size()-1);
            }
            cnt++;
        }
        if(al.size() == 0){
            bw.write(Integer.toString(0));
        }
        else{
            int a = 0;
            for(int i = 0; i<al.size(); i++){
                a += al.get(i);
            }
            bw.write(Integer.toString( a ) );
        }
        bw.flush();

    }
}
