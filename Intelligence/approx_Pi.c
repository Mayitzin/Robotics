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
#define M_PI acos(-1.0f)
#endif // M_PI


// Declare functions
double deg2rad(double d);
long double archimedes(double n);
long double madhava(int K);
long double wallis(int N);
long double bailey(int K);
long double bellard(int K);

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
    printf("   Squared error = %1.5Le\n\n", (pi-M_PI)*(pi-M_PI));
    // Madhava-Leibniz formula
    pi = madhava((int)n);
    printf("   Madhava(%1.1f) = %1.10Lf\n", n, pi);
    printf("   Squared error = %1.5Le\n\n", (pi-M_PI)*(pi-M_PI));
    // Wallis product
    pi = wallis(n);
    printf("   Wallis(%1.1f) = %1.10Lf\n", n, pi);
    printf("   Squared error = %1.5Le\n\n", (pi-M_PI)*(pi-M_PI));
    // Baileys' sum
    pi = bailey((int)n);
    printf("   Bailey(%1.1f) = %1.10Lf\n", n, pi);
    printf("   Squared error = %1.5Le\n\n", (pi-M_PI)*(pi-M_PI));
    // Bellard's formula
    pi = bellard((int)n);
    printf("   Bellard(%1.1f) = %1.10Lf\n", n, pi);
    printf("   Squared error = %1.5Le\n\n", (pi-M_PI)*(pi-M_PI));

    return 0;
}


/*
 * Convert degrees to radians
**/
double deg2rad(double d) {
    double r;
    r = d*M_PI/180;
    return r;
}


/*
 * Archimedes' method to approximate Pi
**/
long double archimedes(double n) {
    long double pi = n*sin(deg2rad(180/n));
    return pi;
}


/*
 * Madhava-Leibniz Series to approximate Pi
 *
 * see: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
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


/*
 * Wallis product for Pi
 *
 * see: https://en.wikipedia.org/wiki/Wallis_product
**/
long double wallis(int N) {
    int n;
    long double f1, f2, product=1.0;
    for(n=1; n<=N; ++n){
        f1 = (double)(2*n)/(2*n-1);
        f2 = (double)(2*n)/(2*n+1);
        product *= (f1*f2);
    }
    return 2.0*product;
}


/*
 * David H Bailey formula for Pi
 *
 * see: http://www.davidhbailey.com/dhbpapers/pi-quest.pdf
**/
long double bailey(int K) {
    double k;
    double mon1, mon2, mon3, mon4;
    long double suma=0.0;
    for(k=0; k<=K; ++k) {
        mon1 = (4.0/(8.0*k+1.0));
        mon2 = (2.0/(8.0*k+4.0));
        mon3 = (1.0/(8.0*k+5.0));
        mon4 = (1.0/(8.0*k+6.0));
        suma += (1/pow(16,k))*(mon1-mon2-mon3-mon4);
    }
    return suma;
}


/*
 * Improved formula for Pi by Fabrice Bellard
 *
 * see: http://bellard.org/pi/pi_bin.pdf
**/
long double bellard(int K) {
    double k;
    double mon1, mon2, mon3, mon4, mon5, mon6, mon7;
    long double suma=0.0;
    for(k=0; k<=K; ++k) {
        mon1 = 32.0 / (4.0*k+1.0);
        mon2 = 1.0  / (4.0*k+3.0);
        mon3 = 256.0/ (10.0*k+1.0);
        mon4 = 64.0 / (10.0*k+3.0);
        mon5 = 4.0  / (10.0*k+5.0);
        mon6 = 4.0  / (10.0*k+7.0);
        mon7 = 1.0  / (10.0*k+9.0);
        suma += (pow(-1,k)/pow(2,10*k))*(-mon1-mon2+mon3-mon4-mon5-mon6+mon7);
    }
    return suma/64.0;
}