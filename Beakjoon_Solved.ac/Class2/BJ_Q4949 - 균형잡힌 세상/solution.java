import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int no; // no판별
        while(true){
            String s = br.readLine();
            no = 0;
            ArrayList<Character> sl = new ArrayList<Character>();
            if(s.charAt(0) == '.'){
                
                break;
            }
            for(int i = 0; i < s.length(); i++){
                if(s.charAt(i) == '('){
                    sl.add(s.charAt(i));
                }

                else if(s.charAt(i) == '['){
                    sl.add(s.charAt(i));
                }

                else if(s.charAt(i) == ')'){
                    if(sl.size() == 0){
                        no = 1;
                        break;
                    }
                    else{
                        if(sl.get(sl.size() -1) == '('){
                            sl.remove(sl.size()-1);
                        }
                        else{
                            no = 1;
                            break;
                        }
                    }
                    
                }

                else if(s.charAt(i) == ']'){
                    if(sl.size() == 0){
                        no = 1;
                        break;
                    }
                    else{
                        if(sl.get(sl.size() -1) == '['){
                            sl.remove( sl.size() - 1 );
                            
                        }
                        else{
                            no = 1;
                            break;
                        }
                    }
                }
            }
            if(no == 1 || sl.size() != 0){
                bw.write("no" + "\n");
            }
            else
            bw.write("yes" + "\n");
        }

        bw.flush();
    }
}