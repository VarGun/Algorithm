import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> ans = new ArrayList<Integer>();

        int n = sc.nextInt();
        int[] nList = new int[n];
        for(int i = 0; i < n; i++){
            nList[i] = sc.nextInt();
        }
        Arrays.sort(nList);


        int m = sc.nextInt();
        int[] mList = new int[m];
        for(int i = 0; i < m; i++){
            mList[i] = sc.nextInt();
        }

        for(int i = 0; i < m; i++){
            int mi = mList[i];
            int high = n-1;
            int low = 0;
            int cnt = 0;
            while(low <= high){
                int mid = (high + low) /2;
                
                if(mi < nList[mid]){
                    high = mid - 1;
                }

                else if(mi > nList[mid]){
                    low = mid + 1;
                }

                else{
                    cnt = 1;
                    break;
                }
            }
            if(cnt == 1){
                ans.add(1);
            }
            else if(cnt == 0){
                ans.add(0);
            }   

        }
        sc.close();
        for(int i = 0; i < m; i++){
            System.out.println(ans.get(i));
        }
    }
}