/**
 *  Insertion Sort
 *  --------------
 *  Using Standard C99.
 *  Shows every sorting cycle.
 *  Hints:
 *  - ASCII characters from 'A' to 'Z' span from 65 to 90.
 *  See:
 *  [1] http://www.algolist.net/Algorithms/Sorting/Insertion_sort
 *  [2] https://www.youtube.com/watch?v=8oJS1BMKE64
 *
 *  History:
 *      05.02.2015. First implementation.
 *  
 *  @author: Mario Garcia
 *  www.mayitzin.com
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    char temp, s[100];
    int l, c, d;
    
    scanf("%s", s);
    l = strlen(s);
    // If only one character, just print it back
    if (l==1){
        printf("%c\n", s[0]);
    }
    // If chain of characters (string), sort them
    for (c=1 ; c <=l-1; c++) {
        d = c;
        while ( d > 0 && s[d] < s[d-1]) {
            temp   = s[d];
            s[d]   = s[d-1];
            s[d-1] = temp;
            d--;
        }
        printf("%s\n", s);
    }
    
    return 0;
}