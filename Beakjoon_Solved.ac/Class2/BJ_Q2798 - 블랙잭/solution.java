import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<Integer> nL2 = new ArrayList<Integer>();
        ArrayList<Integer> nL = new ArrayList<Integer>();
        String[] s = br.readLine().split(" ");
        String[] s2 = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);

        for(int i = 0 ; i < n ; i++){
            nL2.add(Integer.parseInt(s2[i]));
        }


        Collections.sort(nL2);
        for(int i = 0; i < n - 2; i++){
            for(int j = i + 1; j < n - 1; j++){
                for(int k = j + 1; k < n; k++){
                    if( m - (nL2.get(i) + nL2.get(j) + nL2.get(k)) >=0 ){
                        nL.add((nL2.get(i) + nL2.get(j) + nL2.get(k)));
                    }
                }
            }
        }
        Collections.sort(nL);
        bw.write(Integer.toString(nL.get(nL.size()-1)));
        bw.flush();

    }
}
