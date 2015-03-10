/* Ramanujan Series to Pi (IN PROGRESS)
 * ------------------
 * This code shows the progress of the estimation of Pi based on
 * Ramanujan's series.
 * For example:
 * ./ramanujan_Pi 6
 *
 * For further reference see:
 * [1] http://en.wikipedia.org/wiki/Srinivasa_Ramanujan
 *
 * History:
 * 10.03.2015. First Implementation.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

unsigned long factorial(unsigned long a);

int main(int argc, char *argv[]){
    float n, s, pi;
    long double nomin, denom;
    n = atof(argv[1]);
    union {
        int myInt;
        double myFloat;
    } num_in;

    printf("You wrote %f\n",n);
    s = 0.0;
    for (unsigned long i=0; i<10; i++){
        nomin = factorial(4*i)*(1103 + 26390*(double)i);
        denom = pow((double)factorial(i),4)*pow(396.0,(double)(4*(double)i));
        s = nomin/denom;
        printf("%u\t%f\t%lu\t%lu\n", i, (double)i, factorial(i), s);
    }
    printf("The sum is %lf\n", s);

    s = 1.0;
    pi = 9801.0/(s*2.0*sqrt(2.0));
    printf("The result is: %f\n", pi);

    return 0;
}

unsigned long factorial(unsigned long a){
    unsigned long f = 1;
    for(unsigned long count=1;count<=a; count++){
        f*=count;
    }
    return f;
}
