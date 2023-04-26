import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> pl = new ArrayList<Integer>(); // front 배열
        ArrayList<Integer> pl2 = new ArrayList<Integer>(); // back 배열

        int cnt = 0;
        while(cnt < n){
            int si = pl.size();
            int si2 = pl2.size();
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            if(s.equals("push_front")){
                pl.add(Integer.parseInt(st.nextToken()));
            }
            else if(s.equals("push_back")){
                pl2.add(Integer.parseInt(st.nextToken()));
            }
            else if(s.equals("pop_front")){
                if(si != 0){
                    bw.write(Integer.toString(pl.get(si-1)) + "\n");
                    pl.remove(si-1);
                }
                else{
                    if(si2 == 0){
                        bw.write("-1" + "\n");
                    }
                    else{
                        bw.write(Integer.toString(pl2.get(0)) + "\n");
                        pl2.remove(0);
                    }
                } 
            }
            else if(s.equals("pop_back")){
                if(si2 != 0){
                    bw.write(Integer.toString(pl2.get(si2-1)) + "\n");
                    pl2.remove(si2-1);
                }
                else{
                    if(si == 0){
                        bw.write("-1" + "\n");
                    }
                    else{
                        bw.write(Integer.toString(pl.get(0)) + "\n");
                        pl.remove(0);
                    }
                } 
            }

            else if(s.equals("size")){
                bw.write(Integer.toString(si + si2) + "\n");
            }
            else if(s.equals("empty")){
                if(si + si2 == 0){
                    bw.write("1" + "\n");
                }
                else
                bw.write("0" + "\n");
            }
            else if(s.equals("front")){
                if(si != 0){
                    bw.write(Integer.toString(pl.get(si-1)) + "\n");
                }
                else{
                    if(si2 == 0){
                        bw.write("-1" + "\n");
                    }
                    else{
                        bw.write(Integer.toString(pl2.get(0)) + "\n");
                    }
                }
            }
            else if(s.equals("back")){
                if(si2 != 0){
                    bw.write(Integer.toString(pl2.get(si2-1)) + "\n");
                }
                else{
                    if(si == 0){
                        bw.write("-1" + "\n");
                    }
                    else{
                        bw.write(Integer.toString(pl.get(0)) + "\n");
                    }
                } 
            }
            cnt++;
        }

        bw.flush();
    }
}
