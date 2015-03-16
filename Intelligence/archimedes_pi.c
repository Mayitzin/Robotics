/* Archimides Method to estimate Pi
 * --------------------------------
 * This function approximates the value of Pi using Archimedes' method.
 *
 * History:
 * 14.03.2015. First Implementation.
 * 16.03.2015. Added Comments and Input error detection.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265359

double rad2deg(double r);
double deg2rad(double d);

int main(int argc, char *argv[]){
    double n, pi;

    if (argc<2){
        printf("[ERROR]\nUsage:\t./archimedes_pi n\n");
        printf("\twhere n is a positive definite integer\n");
        exit(1);
    }
    n = atof(argv[1]);

    // Archimedes Method
    pi = n*sin(deg2rad(180/n));
    printf("Archimedes' estimation of Pi with n = %.0f is:\n", n);
    printf("%.10f\n", pi);

    return 0;
}

double rad2deg(double r){
    double d;
    d = r*180.0/PI;
    return d;
}

double deg2rad(double d){
    double r;
    r = d*PI/180;
    return r;
}