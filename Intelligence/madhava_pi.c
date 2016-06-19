/*
 * Madhava-Leibniz Series to approximate Pi
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
#include <stdlib.h>   // atof
#include <math.h>     // sqrt, acosf, pow

// Define Constants
#define SQ12 sqrt(12.0f)

// Define Pi, because C99 dropped it out
#ifndef M_PI
#define M_PI acosf(-1.0f)
#endif // M_PI

// Declare function
long double madhava(int K);


// Main routine
int main(int argc, char *argv[]){
    int K = 5;

    if (argc<2)
    	printf("No input given. Using default K=5.\n");
    else
    	K = atoi(argv[1]);

    long double mad_value = madhava(K);
    printf("Madhava(%d) = %1.10Lf\n", K, mad_value);
    printf("Squared error = %Le\n", (mad_value-M_PI)*(mad_value-M_PI));

    return 0;
}


// Definition of Madhava function
long double madhava(int K) {
    int k=0;
    long double num, den, suma=0.0;
    for(k=0; k<=K; ++k){
        num = pow(-3.0f, -k);
        den = (long double)(2*k+1);
        suma += num / den;
    }
    suma *= SQ12;
    return suma;
}