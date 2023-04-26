import java.util.Scanner;
import java.util.ArrayList;

public class solutionMe {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = 0;
        a = sc.nextInt();
        String b = "";
        ArrayList<String> sL2 = new ArrayList<String>();
        for(int i = 0; i < a; i++){
            b = sc.next();
            if(!sL2.contains(b)){
                sL2.add(b);
            }
        }
        sc.close();
        String[] sL = new String[sL2.size()];

        for(int i = 0 ; i < sL2.size(); i++){
            sL[i] = sL2.get(i);
        }
        
        String temp = sL[0];
        
        for(int i = 0; i<sL.length; i++){
            for(int j = i+1; j < sL.length; j++){
                if(sL[i].length() > sL[j].length()){
                    temp = sL[i];
                    sL[i] = sL[j];
                    sL[j] = temp;
                }
            }
        }
        

        for(int i = 0; i < sL.length; i++){
            for(int j = i+1; j < sL.length; j++){
                if(sL[i].length() == sL[j].length()){
                    if(sL[i].compareTo(sL[j]) != 1){
                    temp = sL[i];
                    sL[i] = sL[j];
                    sL[j] = temp;
                    }
                }
            }
        }
        
        for(int i = 0; i<sL.length; i++){
            System.out.println(sL[i]);
        }
    }
}

