import java.util.*;
import java.io.*;

public class solution {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = sc.nextInt();
        int k = sc.nextInt();
        Queue<Integer> nQ = new LinkedList<Integer>();
        for(int i = 0; i < n; i++ ){
            nQ.add(i+1);
        }
        bw.write("<");
        while(nQ.size() > 1){
            for(int i = 0 ; i < k - 1; i++){
                nQ.offer(nQ.poll());
            }
            bw.write(Integer.toString(nQ.poll()) + ", ");
        }
        sc.close();
        bw.write(Integer.toString(nQ.poll()) + ">");
        bw.flush();

    }
}
