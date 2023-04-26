import java.io.*;

public class solution {
    public static void main(String[] args) throws IOException{
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        int[] fibo = new int[40];
        fibo[0] = 1;
        fibo[1] = 1;
        for(int j = 2; j < 40; j++){
            fibo[j] = fibo[j - 1] + fibo[j - 2];
        }
        for(int i = 0; i < t; i++){
            int c = Integer.parseInt(br.readLine());
            if(c == 0){
                bw.write(Integer.toString(1) + " " + Integer.toString(0) + "\n");
            }
            else if(c == 1){
                bw.write(Integer.toString(0) + " " + Integer.toString(1) + "\n");
            }
            else
            bw.write(Integer.toString(fibo[c-2]) + " " + Integer.toString(fibo[c-1]) + "\n");
        }
        bw.flush();

    }
}
