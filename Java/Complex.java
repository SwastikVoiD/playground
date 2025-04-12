import java.util.Scanner;

class Complex {
    private double real; 
    private double imaginary;
    // Constructor
    public Complex(double r, double i){ 
        this.real = r;
        this.imaginary = i;
    }
    // Method to add two complex numbers
    public Complex add(Complex other){ 
        return new Complex(this.real + other.real, this.imaginary + other.imaginary);
    }
    // Method to multiply two complex numbers
    public Complex multiply(Complex other) { 
        double newReal = this.real * other.real - this.imaginary * other.imaginary;
        double newImaginary = this.real * other.imaginary +this.imaginary * other.real; 
        return new Complex(newReal, newImaginary); 
    }
    // Method to display a complex number
    public void display() {
        if (imaginary >= 0) {
            System.out.printf("%.2f + %.2fi", real, imaginary);
        } 
        else {
            System.out.printf("%.2f - %.2fi", real, Math.abs(imaginary));
        }
    }
    // Method for matrix addition (only for same-sized matrices)
    public static Complex[][] matrixAddition(Complex[][] A, Complex[][] B) {
        int rows = A.length; 
        int cols = A[0].length; 
        Complex[][] result = new Complex[rows][cols]; 
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) { 
                result[i][j] = A[i][j].add(B[i][j]); 
            } 
        } 
        return result; 
    }
    // Method for matrix multiplication (A[m x n] * B[n x p] = C[m x p])
    public static Complex[][] matrixMultiplication(Complex[][] A, Complex[][] B) { 
        int rowsA = A.length; 
        int colsA = A[0].length;
        int rowsB = B.length; 
        int colsB = B[0].length; 
        if (colsA != rowsB) { 
            System.out.println("Matrix multiplication is not possible (Columns of A must match Rows of B)."); 
            return null;
        } 
        Complex[][] result = new Complex[rowsA][colsB]; 
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                result[i][j] = new Complex(0, 0); 
                for (int k = 0; k < colsA; k++) {
                    result[i][j] = result[i][j].add(A[i][k].multiply(B[k][j]));
                } 
            }
        }
        return result;
    }

    // Method to display a matrix of complex numbers
    public static void displayMatrix(Complex[][] matrix) {
        for (Complex[] row : matrix) { 
            for (Complex c : row) { 
                c.display();
                System.out.print("\t");
            } 
            System.out.println();
        }
    } 
    public static void main(String[]args) {
        Scanner scanner = new Scanner(System.in);
        // Input matrix A
        System.out.print("Enter size of Matrix A (rows and columns): "); 
        int rowsA = scanner.nextInt(); 
        int colsA = scanner.nextInt(); 
        Complex[][] matrixA = new Complex[rowsA][colsA]; 
        System.out.println("Enter elements for Matrix A (real and imaginary parts):"); 
        for (int i = 0; i < rowsA; i++) { 
            for (int j = 0; j < colsA;j++) {
                double real = scanner.nextDouble();
                double imag = scanner.nextDouble();
                matrixA[i][j] = new Complex(real, imag);
            }
        }
        // Input matrix B
        System.out.print("Enter size of Matrix B (rows and columns): ");
        int rowsB = scanner.nextInt();
        int colsB = scanner.nextInt();
        Complex[][] matrixB = new Complex[rowsB][colsB]; 
        System.out.println("Enter elements for Matrix B (real and imaginary parts):"); 
        for (int i = 0; i < rowsB; i++) { 
            for (int j = 0; j < colsB; j++) { 
                double real = scanner.nextDouble();
                double imag = scanner.nextDouble(); 
                matrixB[i][j] = new Complex(real, imag); 
            }
        }
        // Display input matrices
        System.out.println("Matrix A:"); 
        displayMatrix(matrixA); System.out.println("Matrix B:"); 
        displayMatrix(matrixB);
        // Perform matrix addition (only if A and B have the same dimensions)
        if (rowsA == rowsB && colsA == colsB) { 
            Complex[][] sumMatrix = matrixAddition(matrixA, matrixB); 
            System.out.println("Sum of Matrices:");
            displayMatrix(sumMatrix); 
        } 
        else { 
            System.out.println("Matrix addition is not possible (both matrices must have the same dimensions).");
        }
        // Perform matrix multiplication
        Complex[][] productMatrix = matrixMultiplication(matrixA, matrixB); 
        if (productMatrix != null) { 
            System.out.println("Product of Matrices:");
            displayMatrix(productMatrix); 
        } 
        scanner.close();
    }
}
