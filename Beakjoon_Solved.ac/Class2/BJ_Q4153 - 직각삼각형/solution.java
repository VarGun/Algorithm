import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while(true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            ArrayList<Integer> al = new ArrayList<Integer>();
            al.add(Integer.parseInt(st.nextToken()));
            al.add(Integer.parseInt(st.nextToken()));
            al.add(Integer.parseInt(st.nextToken()));

            if(al.get(0) == 0){
                break;
            }
            Collections.sort(al);
            
            if(Math.pow(al.get(2), 2) == Math.pow(al.get(0), 2) + Math.pow(al.get(1), 2)){
                bw.write("right" + "\n");
            }
            else
            bw.write("wrong" + "\n");
        }
        bw.flush();


    }
}
