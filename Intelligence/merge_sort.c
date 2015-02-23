/**
 *  Merge Sort
 *  -----------
 *  Using Standard C99.
 *  Hints:
 *  - ASCII characters from 'A' to 'Z' span from 65 to 90.
 *  See:
 *  [1] http://en.wikipedia.org/wiki/Merge_sort
 *  [2] https://www.youtube.com/watch?v=ZRPoEKHXTJg
 *
 *  History:
 *      14.02.2015. First implementation.
 *      23.02.2015. Changed maximum allowed to 100.
 *  
 *  @author: Mario Garcia
 *  www.mayitzin.com
 */

#include <stdio.h>
#include <string.h>
#define MAX 100

void conquer(char arr[], int low, int mid, int high);
void divide(char arr[], int low, int high);

int main(){
    char s[MAX];
    int i,n;

    printf("Enter the elements which to be sort:\n");
    scanf("%s", s);             // Read input string
    n = strlen(s);              // Length of string

    divide(s,0,n-1);

    for(i=0;i<n;i++){
        printf("%c",s[i]);
    }
    printf("\n");

   return 0;
}

void divide(char arr[], int low, int high){
    int mid;
    // Repeatedly break the sequence to smalles pair of elements
    if(low<high){
        mid = (low+high)/2;
        divide(arr,low,mid);
        divide(arr,mid+1,high);
        conquer(arr,low,mid,high);
    }
}

void conquer(char arr[], int low, int mid, int high){
    int i,m,k,l,temp[MAX];

    l = low;
    i = low;
    m = mid+1;

    while((l<=mid)&&(m<=high)){
        if(arr[l]<=arr[m]){
            temp[i]=arr[l];
            l++;
        }
        else{
            temp[i]=arr[m];
            m++;
        }
        i++;
    }

    if(l>mid){
        for(k=m;k<=high;k++){
            temp[i]=arr[k];
            i++;
        }
    }
    else{
        for(k=l;k<=mid;k++){
            temp[i]=arr[k];
            i++;
        }
    }
   
    for(k=low;k<=high;k++){
        arr[k]=temp[k];
    }
}