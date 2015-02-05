/**
 *  Bubble Sort
 *  -----------
 *  Using Standard C99.
 *  Shows every sorting cycle.
 *  Hints:
 *  - ASCII characters from 'A' to 'Z' span from 65 to 90.
 *  See:
 *  [1] http://www.algolist.net/Algorithms/Sorting/Bubble_sort
 *  [2] https://www.youtube.com/watch?v=Cq7SMsQBEUw
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
    
    printf("Enter elements\n");
    scanf("%s", s);
    l = strlen(s);
    
    // printf("Enter %d integers\n", l);
    
    // for (c = 0; c < l; c++) {
    //     scanf("%d", &array[c]);
    // }
    
    for (c = 1 ; c <= l - 1; c++) {
        d = c;
        while ( d > 0 && s[d] < s[d-1]) {
            temp   = s[d];
            s[d]   = s[d-1];
            s[d-1] = temp;
            d--;
        }
        printf("%s\n", s);
    }
    
    printf("Sorted list in ascending order:\n");
    
    // for (c = 0; c <= l - 1; c++) {
    //     printf("%s", s[c]);
    // }
    printf("%s\n", s);
    
    return 0;
}