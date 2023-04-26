import java.util.Scanner;


public class solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = 0;
        int n = 0;
        m = sc.nextInt();
        n = sc.nextInt();
        String s = "";
        char[][] chess = new char[m][n];
        for(int i = 0; i < m; i++){
            s = sc.next();
            for(int j = 0; j < n; j++){
                chess[i][j] = s.charAt(j);
            }
        }

        char[][] Bchess = new char[8][8];
        char[][] Wchess = new char[8][8];

        for(int i = 0; i < 8; i++){
            for(int j = 0 ; j < 8; j++){
                if(i % 2 == j % 2 ){
                    Bchess[i][j] = 'B';
                    Wchess[i][j] = 'W';
                }
                else{
                    Bchess[i][j] = 'W';
                    Wchess[i][j] = 'B';
                }

            }

        }

        int ans = 2147483647;
        int ans2 = 0;
        int ans3 = 0;
        int ans4 = 0;

        for(int i = 0; i < m - 7; i++){
            for(int j = 0; j < n - 7; j++){
                ans2 = 0;
                ans3 = 0;
                ans4 = 0;
                for(int k = 0; k < 8; k++){
                    for(int l = 0; l < 8; l++){
                        if(chess[k+i][l+j] != Wchess[k][l]){
                            ans2 += 1;
                        }
                        if(chess[k+i][l+j] != Bchess[k][l]){
                            ans3 += 1;
                        }
                    }
                }

                if(ans2 < ans3){
                    ans4 = ans2;
                }
                else{
                    ans4 = ans3;

                }

                if(ans4 < ans){
                    ans = ans4;
                }
            }
        }

        System.out.println(ans);
        


    }
}
