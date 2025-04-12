import java.util.Scanner;

public class HollowSquarePattern {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input from user
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();

        // Generate hollow square pattern
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Print number on borders
                if (i == 0 || i == n - 1 || j == 0 || j == n - 1) {
                    System.out.print(n + " ");
                } else {
                    System.out.print("  "); // 2 spaces for alignment
                }
            }
            System.out.println();
        }

        scanner.close();
    }
}
