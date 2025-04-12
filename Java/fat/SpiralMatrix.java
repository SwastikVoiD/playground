

public class SpiralMatrix {
    public static void main(String[] args) {
        int n = 4; // You can change this to any size
        int[][] matrix = new int[n][n];

        int value = 1;
        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;

        while (top <= bottom && left <= right) {
            // Top row
            for (int i = left; i <= right; i++) {
                matrix[top][i] = value++;
            }
            top++;

            // Right column
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = value++;
            }
            right--;

            // Bottom row
            for (int i = right; i >= left; i--) {
                matrix[bottom][i] = value++;
            }
            bottom--;

            // Left column
            for (int i = bottom; i >= top; i--) {
                matrix[i][left] = value++;
            }
            left++;
        }

        // Printing the matrix
        for (int[] row : matrix) {
            for (int num : row) {
                System.out.printf("%3d ", num);
            }
            System.out.println();
        }
    }
}
