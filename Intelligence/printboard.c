/* Checker Board Printer
 * 
 * History:
 *     17.10.2015. First implementation.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
#include <string.h>

#define cellSize 5

int main(int argc, char *argv[]){
	char input[];
	fgets(input, sizeof(argv[1]), argv[1]);
	printf("%s\n", input);
}