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

int main(){
    char temp, s[100];
    int l, i, j;
    bool swap=false;
    
    scanf("%s", s);             // Read input string
    l = strlen(s);              // Length of string
    // If only one character, just print it back
    if (l==1){
        printf("%c\n", s[0]);
    }
    // If chain of characters (string), sort them
    else if (l>1){
        for (j=0; j<=i^2; j++){ // Limit j=i^2 because O(n^2)
            swap = false;
            for (i=0; i<=l; i++) {
                if ((s[i]>s[i+1]) && (s[i+1]!=0)) {
                    temp = s[i+1];
                    s[i+1] = s[i];
                    s[i] = temp;
                    swap = true;
                }
            }
            if (swap==true){    // Print re-sorted chain
                printf("%s\n", s);
            }
            else {
                break;
            }
        }
    }

    return(0);
}