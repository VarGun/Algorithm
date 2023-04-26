import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> nL = new ArrayList<Integer>();
        for(int i = 0; i < n; i++){
            int a = Integer.parseInt(br.readLine());
            nL.add(a);
        }
        Collections.sort(nL);
        for(int i = 0; i < n; i++){
            bw.write(nL.get(i) + "\n");
        }
        bw.flush();


    }
}
