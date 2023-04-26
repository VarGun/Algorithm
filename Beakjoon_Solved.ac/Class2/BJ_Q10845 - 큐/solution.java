import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> pl = new ArrayList<Integer>();
        int cnt = 0;
        while(cnt < n){
            int si = pl.size();
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            if(s.equals("push")){
                pl.add(Integer.parseInt(st.nextToken()));
            }
            else if(s.equals("pop")){
                if(si != 0){
                    bw.write(Integer.toString(pl.get(0)) +"\n");
                    pl.remove(0);
                }
                else
                bw.write("-1" + "\n");
            }
            else if(s.equals("size")){
                bw.write(Integer.toString(si) + "\n");
            }
            else if(s.equals("empty")){
                if(si == 0){
                    bw.write("1" + "\n");
                }
                else
                bw.write("0" + "\n");
            }
            else if(s.equals("front")){
                if(si == 0){
                    bw.write("-1" + "\n");
                }
                else
                bw.write(Integer.toString(pl.get(0)) + "\n");
            }
            else if(s.equals("back")){
                if(si == 0){
                    bw.write("-1" + "\n");
                }
                else
                bw.write(Integer.toString(pl.get(si-1)) + "\n");
            }
            cnt++;
        }

        bw.flush();
    }
}
