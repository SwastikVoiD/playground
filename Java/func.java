import java.util.*;
public class func {
    public static void main(String args[]){

        Scanner input = new Scanner(System.in);

        System.out.println("How many Rows in first matrix?");
        int r1 = input.nextInt();
        System.out.println("How many Columns in first matrix?");
        int c1 = input.nextInt();
        int arr1[][] = new int[r1][c1];
        
        System.out.println("How many Rows in second matrix?");
        int r2 = input.nextInt();
        System.out.println("How many Columns in second matrix?");
        int c2 = input.nextInt();
        int arr2[][] = new int[r2][c2];

        for(int i = 0; i < r1; i++){
            for(int j = 0; j < c1; j++){
                System.out.println("Enter element" );
                arr1[i][j] = input.nextInt();
            }
        }

        for(int i = 0; i < r2; i++){
            for(int j = 0; j < c2; j++){
                System.out.println("Enter element" );
                arr2[i][j] = input.nextInt();
            }
        }

        for(int i = 0; i < r1; i++){
            for(int j = 0; j < c1; j++){
                System.out.print(arr1[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println();

        for(int i = 0; i < r2; i++){
            for(int j = 0; j < c2; j++){
                System.out.print(arr2[i][j] + " ");
            }
            System.out.println();
        }

        if (c1 == r2){
            int arr3[][] = new int[r1][c2];

            for(int i = 0; i< r1; i++){
                for(int j = 0; j < c2; j++){
                    for(int k = 0; k < c1; k++){
                        arr3[i][j] += arr1[i][k] + arr2[k][j];
                    }
                }
            }
            System.out.println("The product is :");

            for(int i = 0; i < r2; i++){
                for(int j = 0; j < c2; j++){
                    System.out.print(arr3[i][j] + " ");
                }
                System.out.println();
            }
        }
        else {
            System.out.println("Multiplication not possible");
        }


    }
        
}
