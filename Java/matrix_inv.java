import java.util.Scanner;

public class matrix_inv {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of rows:\t");
        int n = input.nextInt();
        System.out.println();

        System.out.print("Enter the number of columns:\t");
        int m = input.nextInt();

        int arr[][] = new int[n][m];

        for(int i = 0; i < n; i++){
            for(int j = 0; j <m; j++){
                arr[i][j] = input.nextInt();
            }
        }

        if (n == m){
            
        }
        else{
            System.out.println("Inverse cannot be found");
        }

    }

}
