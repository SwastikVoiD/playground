// import java.util.Scanner;

public class pattern1 {
    public static void main(String a[]){
        char arr[][] = new char[3][3];
        for(int i = 0; i<3;i++){
            for (int j = 0; j<3;j++){
                arr[i][j] = '*';
            }
        }
        for (int i = 2; i>=0;i --){
            for (int j =2; j>=0;j--){
                if(i<=j){
                    System.out.print(arr[i][j]+ " ");
                }

            }
            System.out.println();
        }
        for (int i = 1; i<3;i++){
            for (int j = 0;j<3;j++){
                if (i <=j){
                    System.out.print(arr[i][j]+ " ");

                }
            }
            System.out.println();
        }
    }
}
