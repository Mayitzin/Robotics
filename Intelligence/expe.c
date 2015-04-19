/* Exponential Approximation
 * -------------------------
 *
 * Numerical approximation to the value of the exponential constant e.
 *
 * History:
 *     19.04.2015. First implementation.
 *
 * @author: Mario Garcia.
 * www.mayitzin.com
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]){
    double n, r;

    if (argc!=2){
        printf("[ERROR]\nUsage:\t./expe n\n");
        printf("\twhere n is a positive definite integer\n");
        exit(1);
    }

    n = atof(argv[1]);
    r = pow(1+(1/n),n);
    printf("e ~= %f\n", r);

    
    return 0;
}