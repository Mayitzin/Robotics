/* Fibonacci series
 * This is a simple Fibonacci series generator
 * 
 * History:
 *     02.02.2015. First implementation.
 *     07.04.2015. Added comments.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int i=1, n, a=0, b=1, c=0;
    // Change default value if a new given
    if (argc<2){
        printf("[Error] - Usage example:\t./fibonacci 10\n");
        exit(1);
    }
    if (argc>=2){
        n = atoi(argv[1]);
    }
    printf("%d %d ", a, b); /* displaying first two terms */
    for (i; i<=n ; i++ ){
        c = a + b;
        a = b;
        b = c;
        printf("%d ", c);
    }
    return 0;
}
