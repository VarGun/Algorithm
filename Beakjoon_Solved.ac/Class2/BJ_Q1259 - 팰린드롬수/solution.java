import java.util.*;

import java.io.*;


public class solution {
    /*
    public void palindrome(int n){
        String s = Integer.toString(n);
        int a = 0;
        if(s.length() % 2 != 0){
            for(int i = 0; i < s.length() / 2 ; i++){
                if(s.charAt(i) != s.charAt(s.length() -1 - i)){
                    a = 1;
                }
            }
        }
        else{
            for(int i = 0; i < s.length()/2 ; i++){
                if(s.charAt(i) != s.charAt(s.length() -1 - i)){
                    a = 1;
                }
            }
        }
        if(a == 1){
            System.out.println("no");
        }
        else{
            System.out.println("yes");
        }

    }
    */
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = 0;
        ArrayList<String> aList = new ArrayList<String>();

        while(true){
            n = Integer.parseInt(br.readLine());
            if(n == 0){
                break;
            }
            String s = Integer.toString(n);
            String ans = "yes";
            if(s.length() % 2 != 0){
                for(int i = 0; i < s.length() / 2 ; i++){
                    if(s.charAt(i) != s.charAt(s.length() -1 - i)){
                        ans = "no";
                    }
                }
            }
            else{
                for(int i = 0; i < s.length()/2 ; i++){
                    if(s.charAt(i) != s.charAt(s.length() -1 - i)){
                        ans = "no";
                    }
                }
            }
            aList.add(ans);

        }
        for(int i = 0; i<aList.size(); i++){
            System.out.println(aList.get(i));
        }
        br.close();
    }
}
