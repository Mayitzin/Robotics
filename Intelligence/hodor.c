/* Hodor Translator
 * 
 * History:
 *     08.04.2015. First implementation.
 *     13.04.2015. Using memory allocation for string.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_LENGTH 200    // Max num of characters per line
// #define FILE_LENGTH 250    // Max number of lines per file

int main(int argc, char *argv[]) {
    char *token;
    // Allocate memory and check if okay.
    char *text = malloc (LINE_LENGTH);
    if (text == NULL) {
        printf ("No memory\n");
        return 1;
    }
    // Ask user for text, with size limit.
    printf("Enter text to translate:\n");
    fgets(text, LINE_LENGTH, stdin);
    // Remove newline, if any.
    if ((strlen(text)>0) && (text[strlen (text) - 1] == '\n'))
        text[strlen (text) - 1] = '\0';

    // Separate string in defined tokens
    token = strtok(text," ,.-");
    while (token != NULL) {
        printf("Hodor ");
        token = strtok(NULL, " ,.-");
    }
    printf("\n");
    // Free memory and exit.
    free (text);

    return(0);
}