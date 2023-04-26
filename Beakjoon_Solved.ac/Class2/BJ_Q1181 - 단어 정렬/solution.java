import java.util.*;
import java.io.*;
 
public class solution {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        HashSet<String> set = new HashSet<String>();
 
        for(int i=0; i < N; i++) 
            set.add(br.readLine());
        
        ArrayList<String> list = new ArrayList<String>(set);
 
        Collections.sort(list, new Comparator<String>() {
            public int compare(String v1, String v2) {
                if(v1.length() > v2.length()) 
                    return 1; // 길이에 따라 정렬
                else if(v1.length() < v2.length()) 
                    return -1; // 길이에 따라 정렬
                else
                    return v1.compareTo(v2); // 길이가 같으면 사전순으로 정렬
            }
        });
 
        for(String s : list) 
            System.out.println(s);
    }
}