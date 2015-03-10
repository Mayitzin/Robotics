/* Factorial Computation
 * ------------------
 * This code shows the values of the factorial integers up to a number n
 * defined by the user.
 * For example:
 * ./factorial 6
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

unsigned long factorial(int a);

int main(int argc, char *argv[]){
    unsigned long n;
    n = atoi(argv[1]);

    printf("The factorial %lu! is obtained as:\n",n);
    for (int i=1; i<=n; i++){
        printf("%u\t%lu\n", i, factorial(i));
    }

    return 0;
}

unsigned long factorial(int a){
    unsigned long f = 1;
    for(int count=1;count<=a; count++){
        f*=count;
    }
    return f;
}
