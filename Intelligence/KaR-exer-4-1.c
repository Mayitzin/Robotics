/* Exercise 4.1 from K&R
 * ---------------------
 * Modified version from www.c-program-example.com
 *
 * This version removes the use of getch(), which is obtain from the
 * library conio.h, whose use is originally intended for old MS-DOS.
 *
 * Compiled with GCC v.4.9.2 using Standard C99.
 * 
 * History:
 *     16.03.2015. First implementation.
 *
 * @author: Mario Garcia.
 * www.mayitzin.com
**/
 
#include <stdio.h>

int strindex(char s[], char t[]);

int main() {
    int flag=0;
    char str[80],search[10];

    puts("Enter a string:");
    gets(str);
    
    puts("Enter search substring:");
    gets(search);

    flag = strindex(str, search);

    if (flag == -1)
        printf("SEARCH UNSUCCESSFUL! AND POSITION IS:%d",flag);
    else
        printf("SEARCH SUCCESSFUL! AND POSITION IS:%d",flag);
    return 0;
}
 
//strindex: returns the right most index of t in s, -1 if none
int strindex(char s[], char t[]) {
    int k,i,j,pos;
    pos = -1;
    for(i=0; s[i]!='\0'; i++) {
        for(j=i, k=0; t[k]!='\0' && s[j]==t[k]; j++, k++)
            ;
        if (k > 0 && t[k] == '\0')
            pos = i;
    } 
    return pos;
}