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
 *  History:
 *      04.02.2015. First implementation.
 *      05.02.2015. Chaged 'for' loop to 'while' condition.
 *  
 *  @author: Mario Garcia
 *  www.mayitzin.com
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#define MAX 100

int main(){
    char temp, s[MAX];
    int l, i, j;
    bool swap=true;

    scanf("%s", s);             // Read input string
    l = strlen(s);              // Length of string
    // If only one character, just print it back
    if (l==1){
        printf("%c\n", s[0]);
    }
    // If chain of characters (string), sort them
    while ((swap==true) && (l>1)){
        swap = false;
        for (i=0; i<=l-1; i++) {
            if ((s[i]>s[i+1]) && (s[i+1]!=0)) {
                temp = s[i+1];
                s[i+1] = s[i];
                s[i] = temp;
                swap = true;
            }
        }
        // Print re-sorted chain
        if (swap==true){
            printf("%s\n", s);
        }
    }

    return(0);
}