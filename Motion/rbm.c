/**
 * Rigid Body Motion
 *
 * @brief Collection of functions for Rigid Body Motion operations
 *
 * @author Mario Garcia
 * www.mayitzin.com
 */

#include <stdio.h>
#include <math.h>

#define PI 3.1415926538f
#define size 3

int dim_x, dim_y;

int * initZeros(int y, int x);
float * eye(int x);
void printMatrix(int *matrix);
void printMatrixf(float *matrix, int dim_x, int dim_y);
void printMatrixElems(int *matrix);

int main(int argc, char *argv[]){
    if(argc>1){
        dim_y = atoi(argv[1]);
        dim_x = atoi(argv[2]);
    } else {
        dim_y = size;
        dim_x = size;
    }

    float matrix[dim_x][dim_x];
    float *m_ptr;
    m_ptr = &matrix[0][0];
    int i;
    for(i=0; i<(dim_x*dim_x); ++i){
        if (i%(dim_x+1)) {
            *(m_ptr+i) = 0.0f;
        } else {
            *(m_ptr+i) = 1.0f;}
    }
    // for (i=0; i<(dim_x*dim_x); ++i){
    //     printf("%2.4f\n", *(m_ptr+i));
    // }
    printMatrixf(m_ptr, dim_x, dim_y);

    return (0);
}

void printMatrix(int *matrix){
    int i, j;
    for(i=0; i<dim_y; ++i){
        for(j=0; j<dim_x; ++j){
            printf("\t%d", *matrix);
            ++matrix;
        }
        printf("\n");
    }
}

void printMatrixf(float *matrix, int dim_x, int dim_y){
    int i, j;
    for(i=0; i<dim_y; ++i){
        for(j=0; j<dim_x; ++j){
            printf("\t%2.6f", *matrix);
            ++matrix;
        }
        printf("\n");
    }
}

void printMatrixElems(int *matrix){
    int i, j;
    // Print the elements
    for(i=0; i<dim_y; ++i){
        for(j=0; j<dim_x; ++j){
            printf("0x%p : M[%d][%d] = %d\n", matrix, i, j, *matrix);
            ++matrix;
        }
    }
}

int * initZeros(int y, int x){
    int matrix[x][y];
    int *m_ptr;
    m_ptr = &matrix[0][0];
    int i;
    // Set values for each element
    for(i=0; i<(x*y); ++i){
        *(m_ptr+i) = 0;
    }
    return (m_ptr);
}

float * eye(int x){
    float matrix[x][x];
    float *m_ptr;
    m_ptr = &matrix[0][0];
    int i;
    // Set zeros for each element
    for(i=0; i<(x*x); ++i){
        if (i%4) {
            *(m_ptr+i) = 1.0f;
        } else {
            *(m_ptr+i) = 0.0f;}
    }

    // // Set ones on the diagonal
    // m_ptr = &matrix[0][0];
    // *(m_ptr) = 1.0f;
    // *(m_ptr+4) = 1.0f;
    // *(m_ptr+8) = 1.0f;

    m_ptr = &matrix[0][0];
    return (m_ptr);
}