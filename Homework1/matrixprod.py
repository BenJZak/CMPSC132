#---------------------------------------------------------------------
# Name: Benjamin Zakielarz
# Email: bjz5259@psu.edu
# Class: CMPSC 132
# Program 1.1
# Due Date: February 06, 2025
#
# Description: This program reads matrices from a file(s) and writes it to the console IF the user inputs ONLY one file as a parameter. If the user enters multiple files as parameters, the program multiplies them all and returns a new matrix that is the multiplied result of all matrices in the parameter.
#
# Acknowledgement:
#https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/ for how to use sys.agrv in order to accept parameters in command line execution of program.
#---------------------------------------------------------------------

import sys

def readmatrix(fname):
    with open(fname, "r") as file:
        lines = file.readlines()

    matrix = []
    for line in lines[1:]:  #Skip the first line
        matrix.append([int(num) for num in line.split()])

    return matrix

def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Initialize result matrix with zeros as placeholders
    result_matrix = [[0] * cols_B for i in range(rows_A)]

    # Matrix multiplication per instruction sheet
    for i in range(rows_A):
        for j in range(cols_B):
            result_matrix[i][j] = sum(A[i][k] * B[k][j] for k in range(cols_A))

    return result_matrix

def main():
    # Basic error checking
    if len(sys.argv) < 2:
        print("Usage: python3 matrixprod.py file1.txt [file2.txt ...]")
        sys.exit(1)

    matrices = [readmatrix(fname) for fname in sys.argv[1:]]

    if len(matrices) == 1:
        # If only one matrix is provided, just print it
        rows, cols = len(matrices[0]), len(matrices[0][0])
        print(f"[{rows}, {cols}]")
        for row in matrices[0]:
            print(row)
    else:
        # Multiply matrices
        result = matrices[0]
        for matrix in matrices[1:]:
            result = multiply_matrices(result, matrix)

        # Print the final multiplied matrix
        rows, cols = len(result), len(result[0])
        print(f"[{rows}, {cols}]")
        for row in result:
            print(row)

if __name__ == "__main__":
    main()
