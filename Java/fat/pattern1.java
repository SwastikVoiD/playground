import java.util.Scanner;
public class pattern1 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number:\t");
        String a = sc.next();
        char b = a.charAt(0);
        int n = Integer.parseInt(a);
        char[][] mat = new char[n][n];
        for(int i = 0; i<n; i++){
            for(int j =0; j<n;j++){
                if(i == 0 || i == n-1){
                    if(j == 0 || j == n-1){
                        mat[i][j] = b;
                    }
                    else{
                        mat[i][j] = ' ';
                    }

                }
                else if(j==0 || j == n-1){
                    mat[i][j] = ' ';

                }
                else{
                    mat[i][j] = b;
                }
                
            }
        }

        for(int i = 0; i<n;i++){
            for(int j = 0; j < n; j++){
                System.out.print(mat[i][j]+ " ");
            }
            System.out.println();
        }
    }    
}
