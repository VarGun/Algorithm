import java.util.*;

import java.io.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> sL = new ArrayList<Integer>(); // 수열
        ArrayList<Integer> num = new ArrayList<Integer>(); // 1 ~ num
        ArrayList<Integer> stack = new ArrayList<Integer>(); // 스택
        ArrayList<String> ans = new ArrayList<String>(); // 정답
        for(int i = 0; i < n; i++){
            sL.add(Integer.parseInt(br.readLine()));
            num.add(i+1);
        }
        int top = 0;
        int cnt = 0;
        while(true){
            if(stack.size() == 0){
                stack.add(num.get(0));
                num.remove(0);
                top = stack.get(stack.size()-1);
                ans.add("+");
                cnt += 1;
            }
            else{
                top = stack.get(stack.size()-1);
                if(top > sL.get(0)){
                    ans.clear();
                    ans.add("NO");
                    break;
                }
                else if(top < sL.get(0)){
                    stack.add(num.get(0));
                    num.remove(0);
                    ans.add("+");
                    cnt += 1;
                }
                else if(top == sL.get(0)){
                    stack.remove(stack.size()-1);
                    ans.add("-");
                    sL.remove(0);
                    cnt += 1;
                }
            }
            if(cnt == n*2){
                break;
            }            
        }        
        for(int i = 0; i < ans.size(); i++){
            System.out.println(ans.get(i));
        }
    }
}
