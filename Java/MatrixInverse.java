import java.util.Arrays;

public class MatrixInverse {
    public static void main(String[] args) {
        double[][] matrix = {
            {4, 7},
            {2, 6}
        };

        double[][] inverse = invertMatrix(matrix);

        if (inverse != null) {
            System.out.println("Inverse of the matrix:");
            for (double[] row : inverse) {
                System.out.println(Arrays.toString(row));
            }
        } else {
            System.out.println("Matrix is singular and cannot be inverted.");
        }
    }

    public static double[][] invertMatrix(double[][] matrix) {
        int n = matrix.length;
        double[][] augmented = new double[n][2 * n];

        // Step 1: Create augmented matrix [A|I]
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                augmented[i][j] = matrix[i][j];  // Copy original matrix
            }
            augmented[i][i + n] = 1;  // Add identity matrix
        }

        // Step 2: Perform row operations to convert A into I
        for (int i = 0; i < n; i++) {
            if (augmented[i][i] == 0) return null; // Singular matrix

            // Normalize the pivot row
            double diag = augmented[i][i];
            for (int j = 0; j < 2 * n; j++) {
                augmented[i][j] /= diag;
            }

            // Eliminate other rows
            for (int k = 0; k < n; k++) {
                if (k != i) {
                    double factor = augmented[k][i];
                    for (int j = 0; j < 2 * n; j++) {
                        augmented[k][j] -= factor * augmented[i][j];
                    }
                }
            }
        }

        // Step 3: Extract the inverse matrix
        double[][] inverse = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                inverse[i][j] = augmented[i][j + n];
            }
        }

        return inverse;
    }
}
