/* Collatz Conjecture
 * ------------------
 * This code shows the progress of the Collatz conjecture.
 * The user has to run its executable with the starting integer.
 * For example:
 * ./collatz 6
 * Its result is a list of the integers until it reaches 1.
 * 6 3 10 5 16 8 4 2 1
 *
 * History:
 * 08.03.2015. First Implementation.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int n;
    n = atoi(argv[1]);

    printf("%d ",n);
    while(n!=1){
        if (n % 2){
            n = 3*n + 1;
            printf("%d ", n);
        } else{
            n = n/2;
            printf("%d ", n);
        }
    }
    printf("\n");

    return 0;
}
