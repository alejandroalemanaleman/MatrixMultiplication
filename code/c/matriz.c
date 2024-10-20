#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

void matrix_multiply(int n) {
    double **a = (double **)malloc(n * sizeof(double *));
    double **b = (double **)malloc(n * sizeof(double *));
    double **c = (double **)malloc(n * sizeof(double *));
    
    for (int i = 0; i < n; ++i) {
        a[i] = (double *)malloc(n * sizeof(double));
        b[i] = (double *)malloc(n * sizeof(double));
        c[i] = (double *)malloc(n * sizeof(double));
    }

    // Inicialización de las matrices
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            a[i][j] = (double)rand() / RAND_MAX;
            b[i][j] = (double)rand() / RAND_MAX;
            c[i][j] = 0;
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        free(a[i]);
        free(b[i]);
        free(c[i]);
    }
    free(a);
    free(b);
    free(c);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <matrix_size>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    if (n <= 0) {
        printf("Invalid matrix size: %d\n", n);
        return 1;
    }

    matrix_multiply(n);
    return 0;
}

