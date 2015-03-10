/* Factorial Computation
 * ------------------
 * This code shows the values of the factorial integers up to a number n
 * defined by the user.
 * For example:
 * ./factorial 6
 *
 * The maximum possible value is 20! It overflows with 21!
 *
 * For further reference see:
 * [1] http://en.wikipedia.org/wiki/Factorial
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

unsigned long long int factorial(int a);

int main(int argc, char *argv[]){
    int n;
    unsigned long long int f;
    n = atoi(argv[1]);

    // Check if it is negative
    if (n<0){
        printf("Sorry, factorials cannot be negative\n");
        return 1;
    }

    // Start the looping
    printf("The factorial %lu! is obtained as:\n",n);
    for (int i=1; i<=n; i++){
        printf("%u\t%llu\n", i, factorial(i));
    }

    return 0;
}

unsigned long long int factorial(int a){
    // This function computes the factorial of the int a
    if (a<0){
        printf("Sorry, factorials cannot be negative\n");
        return 0;
    } else {
        unsigned long long int f = 1;
        for(int count=1;count<=a; count++){
            f*=count;
        }
        return f;
    }
}
