/* CSV files reader
 * This is a simple CSV file reader
 * 
 * History:
 *     13.03.2015. First implementation.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_LENGTH 200    // Max num of characters per line
#define FILE_LENGTH 500    // Max num of lines per file

int main(int argc, char *argv[]) {
    FILE *file;
    char str[LINE_LENGTH];
    char * chunks;
    int line=0, max_lines=10;

    // Change default value if a new given
    if (argc<2){
        printf("[Error] - Usage:\t./csv file.csv\n");
        exit(1);
    }
    if (argc>2){
       max_lines = atoi(argv[2]);
    }
 
    // opening file for reading
    file = fopen(argv[1] , "r");
    if(file == NULL) {
        perror("Error opening file");
        return(-1);
    }
 
    while(fgets(str, FILE_LENGTH, file)){
        printf("%s", str); // str already has \n
        // Separate string in the token ';'
        chunks = strtok(str,";");
        while(chunks != NULL){
            printf("%s\n", chunks);
            chunks = strtok(NULL, ";");
        }
        line++;
        if (line>=max_lines) break;
    }
    
    fclose(file);

    return(0);
}