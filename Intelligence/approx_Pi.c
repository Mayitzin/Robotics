/*
 * Different examples of approximations to Pi
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define Constants
#define SQ12 sqrt(12.0f)

// Define Pi, because C99 dropped it out
#ifndef M_PI
#define M_PI acosf(-1.0f)
#endif // M_PI


// Declare functions
double deg2rad(double d);
double archimedes(double n);
long double madhava(int K);

// Main routine
int main(int argc, char *argv[]){
	double n = 5.0;
    double pi;

    printf("\n  Accuracy of different methods to approximate to Pi\n\n");

    // Check input parameters
    if (argc<2)
        printf("No input given. Using default n=5.\n\n");
    else
        n = atof(argv[1]);

    // Archimedes Method
    pi = archimedes(n);
    printf("   Archimedes(%1.1f) = %1.8Lf\n", n, pi);
    printf("   Squared error  = %1.5Le\n\n", (pi-M_PI)*(pi-M_PI));

    double mad_value = madhava((int)n);
    printf("   Madhava(%1.1f)    = %1.10Lf\n", n, mad_value);
    printf("   Squared error  = %Le\n", (mad_value-M_PI)*(mad_value-M_PI));

    return 0;
}


/*
 * Convert degrees to radians
**/
double deg2rad(double d){
    double r;
    r = d*M_PI/180;
    return r;
}


/*
 * Archimedes' method to approximate Pi
**/
double archimedes(double n){
    double pi = n*sin(deg2rad(180/n));
    return pi;
}


/*
 * Madhava-Leibniz Series to approximate Pi
**/
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