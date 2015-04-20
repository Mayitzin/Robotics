/* CSV files reader
 * This is a simple CSV file reader
 * 
 * History:
 *     20.04.2015. First implementation.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <iostream>
#include <fstream>
#include <string>

#define FILE_LENGTH 5    // Max num of lines per file

using namespace std;

int main(int argc, char* argv[]){
    string line;
    ifstream myfile ("../Data/some.csv");

    if (argc>1){
        cout << "File Name: " << argv[1] << endl;
        ifstream myfile (argv[1]);
    } else {
        cout << "Using default testing file" << endl;
    }

    // ifstream myfile ("../Data/circle.csv");
    if (myfile.is_open()) {
        int i=0;
        while (getline(myfile, line) && i<FILE_LENGTH) {
            cout << i << ": " << line << endl;
            i++;
        }
        myfile.close();
    }
    else cout << "Unable to open file" << endl;
    return 0;
}