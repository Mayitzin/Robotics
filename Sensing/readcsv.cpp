/* CSV files reader
 * This is a simple CSV file reader
 * 
 * History:
 *     20.04.2015. First implementation.
 *     22.04.2015. Using command line input to set parameters.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <iostream>
#include <fstream>
#include <string>

#define FILE_LENGTH 5           // Num of lines per file
#define MAX_FILE_LENGTH 500     // Max num of lines per file

using namespace std;

int main(int argc, char* argv[]){
    string line, fileName;
    int num_lines = 5;
    ifstream csvFile;

    if (argc>1){
        cout << "File Name: " << argv[1] << endl;
        fileName = argv[1];
        if (argc>2) {
            num_lines = stoi(argv[2]);
            if (num_lines>MAX_FILE_LENGTH){
                num_lines = MAX_FILE_LENGTH;
                cout << "A maximum of " << MAX_FILE_LENGTH << " are pemitted" << endl;
            }
        }
    } else {
        cout << "Showing " << num_lines << " lines of the default testing file" << endl;
        fileName = "../Data/circle.csv";
    }

    csvFile.open(fileName.c_str());
    if (csvFile.is_open()) {
        int i=0;
        while (getline(csvFile, line) && i<num_lines) {
            cout << i << ": " << line << endl;
            i++;
        }
        csvFile.close();
    } else {
        cout << "[ERROR] Unable to open file" << endl;
        cout << "\tUsage:\t./readcsv file.csv number_of_lines" << endl;
        return -1;
    }
    return 0;
}