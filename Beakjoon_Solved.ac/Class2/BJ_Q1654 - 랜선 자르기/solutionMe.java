import java.util.*;


public class solutionMe {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        int n, m, o = 0;
        n = sc.nextInt();
        m = sc.nextInt();
        ArrayList<Integer> nlist = new ArrayList<Integer>();
        for(int i = 0; i < n; i++){
            o = sc.nextInt();
            nlist.add(o);
        }
        sc.close();

        Collections.sort(nlist);
        int a = nlist.get(0); // 최솟값
        int b = 0;
        while(true){
            b = 0;
            
            for(int i = 0; i < n; i++){
                b += nlist.get(i) / a;
            }

            if(b >= m){
                break;
            }

            a -= 1;

            if(a == 0){
                break;
            }
            
        }
        System.out.println(a);
    }
}